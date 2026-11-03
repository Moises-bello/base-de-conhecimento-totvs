---
content_hash: 6f0ed8baceae69b7864b97ab2f7196b70fe47998d7e975e357cc0d5b66da5780
fetched_at: '2026-06-29T00:08:15.527248+00:00'
page_id: '244908653'
product: rm
source: tdn-rm
title: NFE0031_Troca_de_Certificado_Digital
type: documentation
url: https://tdn.totvs.com/display/LRM/NFE0031_Troca_de_Certificado_Digital
version: 4
---

|  |  |
| --- | --- |
| **Produto:** | NF-e - Nota Fiscal Eletrônica |
| **Versões:** | Todas |
| **Ocorrência:** | Troca de Certificado Digital |
| **Ambiente:** | Trocar de Certificado Digital |
| **Passo a passo:** | **Introdução:**  Para realizar a emissão de notas fiscais eletrônicas, é necessário utilizar o Certificado Digital, que é a assinatura da empresa na Nota Fiscal Eletrônica. O mesmo possui uma data de validade, e após esta data de validade, é necessário adquirir um novo arquivo certificado e realizar a troca do mesmo no sistema.  **OBSERVAÇÃO: Realize a preparação do certificado digital antes de executar o procedimento. A documentação está disponível no link abaixo:**    **1º Passo:**  O primeiro passo para realizar a troca do certificado digital, é realizar a exclusão dos arquivos referentes ao certificado digital no TSS. Para isto, acesse a pasta raiz de instalação do TSS ( O diretório padrão é C:/totvssped ) e realize a exclusão de TODOS arquivos com a extensão “.PEM” da pasta CERTS:    **OBSERVAÇÃO: Caso existam mais filiais que realizam a emissão de notas fiscais eletrônicas, os arquivos referentes ao certificado digital também serão excluídos no TSS. Após realizar o envio da primeira NF-e ou a execução do processo “Monitor Sefaz”, os arquivos serão recriados.**  **2º Passo:**  Após realizar a exclusão dos arquivos, acesse a pasta BIN, subpasta APPSERVER e abra o arquivo APPSERVER. Este arquivo tem a extensão “Parâmetro de Configuração”.  Realize a exclusão das linhas com as iniciais “CertificateClient” e “Keyclient”, que apontam os arquivos referentes ao certificado na pasta CERTS:    **3º Passo:**  Será necessário reiniciar o serviço TSS para finalizar a exclusão dos arquivos certificado no aplicativo. Acesse o menu Iniciar, Painel de controle, Ferramentas administrativas, serviços. Clique no serviço “TSS” e clique em “Reiniciar”:    **4º Passo:**  Acesse : Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento  | Integrações | Fiscal.  Na etapa 3 – Certificação Digital 1/2 realize o preenchimento do diretório do arquivo certificado digital e senha. Salve os parâmetros avançando até o final.    **Observação: É recomendado para que não haja problemas com o diretório que foi informado nos parâmetros da Filial, que a pasta tenha as devidas permissões:**    **5º Passo:**  Para finalizar a troca do certificado digital, é necessário enviar uma nova NF-E através do menu Vendas | Faturamento | SPED (Estadual) - processos, “Enviar NF-E” ou a execução do processo “Monitor Sefaz”. Após o envio ou a execução do Monitor, serão criados os novos arquivos referentes ao certificado digital. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
