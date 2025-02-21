"""Main app file."""

import streamlit as st

st.set_page_config(page_title="NAGA App", page_icon="🪢",
                   layout="centered")

st.title(":blue[N]anopore :blue[A]ssembly :blue[G]UI :blue[A]pplication (:blue[NAGA])")
st.markdown(''' Welcome to NAGA, a web based application for running
            [Flye](https://github.com/mikolmogorov/Flye) 
            and [MAFFT](https://mafft.cbrc.jp/alignment/server/index.html) of PCR amplified reads based reads.
            This tool was developed for the [Sulentic Lab](https://people.wright.edu/courtney.sulentic). 
            For questions and feature requests, please reach out to Clayton Allex-Buckner (callexbuckner@gmail) for any questions or feature
            requests. Happy assembling!''')

st.divider()

st.header("Upload Reads")
upload_fastq = st.file_uploader("Upload Raw FASTQ",
                                type=['fastq.gz', 'fastq', 'fq.gz', 'fq'],
                                accept_multiple_files=True,
                                help='''Upload Raw FASTQ files for assembly. Files
                                must have one of the following extensions:
                                fastq.gz, fastq, fq.gz, fq. Names will be parsed
                                from FASTQ filenames.''',
                                label_visibility="visible")

st.divider()
st.header("Flye Parameter Selection")

col1, col2 = st.columns(2)

with col1:
    # Type of reads selector
    read_options = [
        "Nano Raw",
        "Nano Corrected",
        "Nano High Quality"
    ]

    read_captions = [
        "ONT regular reads, pre-Guppy5",
        "ONT reads that were corrected with other methods",
        "ONT high quality reads: Guppy5+ SUP or Q20"
    ]

    read_type = st.radio(
        "Read Type",
        options=read_options,
        captions=read_captions
    )
   

with col2:
    genome_size = st.text_input(
        "Enter size of amplicon reads",
        max_chars=5,
        value="15k",
        help='''Estimated genome size. For example:
        15k (15 kilobase pairs), 20m (20 megabase pairs),
        1gb (1 gigabase pairs)''',
        label_visibility="visible"
    )

    polish_iters = st.slider(
        "Polishing Iterations",
        min_value=1,
        max_value=10,
        value=2,
        help='''Select the number of post assembly polishing
        iterations. This helps to correct sequencing errors present
        within the assembly.''',
        label_visibility="visible"
    )

submit_run = st.button(
    "Start Assembly",
    type="primary",
    icon="🚀"
)

if submit_run:
    if not upload_fastq:
        st.error(
            "Please upload your FASTQ files!",
            icon="🚨"
        )
    else:
        container = st.container(border=True)
        container.write("flye --" + str(read_type) + " --iterations " + str(polish_iters))
