#!/bin/bash

if [[ -f 'config/config.sh' ]]; then
    source config/config.sh
fi

runcmd() {
    echo "$@" >&2
    "$@"
}

#java -jar "${sax_jar}" "${init_xml}" "${tei_xsl}" > "${final_xml}" && \
#java -jar "${sax_jar}" "${final_xml}" "${xslfo_xsl}" > "${fo_obj}" && \
runcmd export FOP_OPTS="${fop_opts}" && \
runcmd "${fop_bin}" -c "${fop_conf}" "${fo_obj}" "${pdf_obj}"

if [ -n "$cleanup" ]; then
    rm -f "${fo_obj}"
    rm -f "${final_xml}"
fi
