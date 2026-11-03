---
article_id: 360053669914
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 8ac0fe3dcd4ce67160024135fcc5770c0c1e781625d3dc10f6aaa7c8bba9a59b
fetched_at: '2026-06-28T22:39:58.648682+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE BRASÍLIA/DF
type: support-article
updated_at: '2024-06-19T19:37:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053669914-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-BRAS%C3%8DLIA-DF
---

**Dúvida**Requisitos para transmissão de notas de serviços para Brasília/DF.  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**A Secretaria de Economia do Distrito Federal implantará um novo Sistema de Gestão, Fiscalização e Arrecadação do ISS, em que utilizará modelo próprio para emissão de NFS-e, no padrão ABRASF, que irá substituir a NF-e modelos 55 e 65.  
  
**A partir de 01/01/2023**, o Sistema iniciou a liberação para a emissão de NFS-e via online ou webservice **em ambiente de Produção**, através de certificado digital ou login e senha do responsável legal.  
  
Portanto, para transmissão das notas será utilizado o rdmake NFSEXMLENV e a rotina FISA022:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9633822782487)

#### **O QUE DEVE SER ATUALIZADO?** Detalhes de todas as liberações até o momento e contempladas abaixo: [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=675569850)

**TSS**  
RPO: [MP - TSS - Atualização do Repositório (RPO) do TSS.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)  
SCHEMA: Incluir os arquivos nfse\_v2.04\_5300108.xsd e tss\_nfse\_tipos\_v2.00.xsd do link ([clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1092493#detail/761857)) na pasta schemas do TSS.  
SYSTEM: Incluir os arquivos tssnewnfse.json, tssatuurl.json e nfse\_5300108.cfg do link ([clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1092384)) na pasta system do TSS.  
  
**PROTHEUS**FISA022: Atualizar a rotina de transmissão pelos links de acordo com a release: ([12.1.2210](https://suporte.totvs.com/portal/p/10098/download?e=1085249)) ou ([12.1.2310](https://suporte.totvs.com/portal/p/10098/download#detail/1124963)).  
NFSEXMLENV: Compilar os rdmakes NFSEXMLENV pelo link [clicando aqui.](https://suporte.totvs.com/portal/p/10098/download?e=1091542) (*Qualquer release do Protheus poderá usar esse link, pois não há trava de release).*  
  
**DIFERENÇAS DO SISTEMA ANTIGO x ATUAL:**  
  
**Funcionalidades da NFS-e de Brasília:**Visto que a nota agora não é mais validado pela Sefaz, os **métodos disponíveis** até o momento são: **Emissão e Consulta RPS.** *(Cancelamento e Substituição está temporariamente com problemas do lado da prefeitura).*  
Demais como Inutilização, Carta de Correção, Impressão de Nota e Envio de E-mail para o cliente com PDF e XML não estão mais disponíveis.  
Lembrando que essa limitação não seria do ERP/TSS e sim do sistema utilizado por Brasília.  
  
Abaixo a **documentação** de como poderá ser realizado a **implantação** e suas devidas **funcionalidades:**  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - IMPLANTAÇÃO DE NFSE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006652632-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-IMPLANTA%C3%87%C3%83O-DE-NFSE?source=search)  
  
**Liberação do Ambiente de Homologação:**  
É preciso **solicitar autorização** para o uso do ambiente via WebService através do e-mail [suporte@notaeletronica.com.br](mailto:suporte@notaeletronica.com.br).   
Caso contrário serão retornadas rejeições E157 e L090 que constam no link: [clicando aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=718424514).  
  
**TSS:**As transmissões de NFS-e Brasília agora **serão gravadas exclusivamente nas tabelas SPED051, SPED053 e SPED055 do TSS.**  
Diferentemente de antes serem gravados nas tabelas SPED050, SPED052 e SPED054 e os eventos   
nas tabelas SPED150 e SPED154.  
  
**Modelo do Documento:**Agora será gerado com **modelo 56** nas tabelas do TSS, diferentemente de antes ser gerado como 55.  
  
**Rotina de Transmissão:**Anteriormente era transmitida pela rotina SPEDNFE, agora conforme citado acima, foi inclusa na rotina **FISA022**.  
  
**Rdmakes**:  
Emissão: Não se faz mais o uso do NFESEFAZ e sim do **rdmake NFSEXMLENV.**  
Impressão: Não possui mais opção de impressão, portanto não há rdmakes como haviam anteriormente.  
  
**Sequência de Numeração do RPS**O provedor consiste em números de RPS que **devem primeiro ser solicitados através do portal** no seguinte caminho **“Solicitação de Documentos Fiscais” -> “ Solicitação”**, nesta opção será gerado números de RPS a serem consumidos, exemplo de 1 a 50.  
  
**Série do RPS**O provedor **obrigatoriamente** utiliza como padrão para envio **em homologação e produção a série '3':  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11377648084503)****Espécie do Documento:**Deverá ser utilizado por padrão a espécie do documento como **RPS** ao invés de SPED, exemplo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11654096186775)  
Documentação: [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - COMO CRIAR UMA ESPECIE PARA NFSE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000308521-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-COMO-CRIAR-UMA-ESPECIE-PARA-NFSE?source=search)  
  
**Todos os cadastros devem caracterizar a prestação do serviço que está sendo executado pelo contribuinte, exemplo: Informar os códigos correspondentes nos campos B1\_CODISS, B1\_CNAE, B1\_TRIBMUN e B5\_NBS no Cadastro do Produto.  
  
Contatos do Provedor**suporte@notaeletronica.com.br / suporte.df@notacontrol.com.br Tel.: (67) 3041-2075.  
  
**Material de Apresentação (Webinar):**Clique [aqui](http://suporte.totvs.com/totvs-tdi-files-maps/mapeamentos/portal-anexos/anexos/zendesk/20221208/TTVFLGP1J003-1670519875622-482065.zip) para fazer o download.  
*\*Obs.: Caso não inicie o download automaticamente, poderá colar o link diretamente em uma nova aba.*
