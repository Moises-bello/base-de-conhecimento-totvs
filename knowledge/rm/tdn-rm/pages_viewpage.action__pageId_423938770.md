---
content_hash: 26d0f6a58306423eb95248a6ca80512716a02be121d05d7fc59eb11585661393
fetched_at: '2026-06-29T00:09:28.725748+00:00'
page_id: '423938770'
product: rm
source: tdn-rm
title: Tributos do Produto por Município
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938770
version: 37
---

Nesta opção, são cadastrados os tributos por município relacionados ao produto, que poderão ser utilizados durante suas movimentações. Nesta tela, será possível a inclusão e a visualização de tributos por município e a alíquota referente ao produto, além da definição de incentivo fiscal. Para acessá-la, vá em *Produto | Anexos | Tributo do Produto por Município*.

Clique aqui para visualizar a telaTributos do Produto por MunicípioIdentificaçãoIdentificaçãoIdentificação

**01. Sobre**: Nesta aba é identificado o tributo e o município cujas regras serão configuradas.

**02. Campos**:

Sigla: Referente a sigla do tributo a ser configurado para determinado produto;

Possui Incentivo Fiscal: No que se refere ao envio de informações para o TSS, o sistema considera no envio da NFS-e se a flag “Possui Incentivo” está marcada. Caso afirmativo, será gerado a tag “incentcult”. Caso estiver desmarcada o sistema irá verificar a flag “Incentivo Cultural” no cadastro da Filial no envio da NFS-e, caso nenhuma das flags estiver marcada, a tag não será gerada.

Base Redução ISS (%): O valor informado no campo Base Redução ISS(%) será utilizado no momento da escrituração para redução de base de cálculo. Caso o tributo, diferente do ICMS e IPI, tenha um fator de redução, a rotina de escrituração irá considerar que a base informada no movimento é reduzida e irá calcular o valor isento relacionado. Este valor será informado no campo Isento dos outros tributos.

CNAE: Campo utilizado para o preenchimento do código CNAE (Classificação Nacional de Atividades Econômicas).

Código do Serviço no Município: Campo utilizado para o preenchimento do código de tributação no município.

Código de Serviço Federal: O Código de Serviço Federal no anexo do produto, "tributos do produto por município", flexibiliza a informação, permitindo mais de 5 caracteres e códigos diferentes por município, onde as legislações municipais podem ser diferentes (O preenchimento deve respeitar a máscara definida no Schema conforme cada prefeitura).

Os campos "Código do Serviço no Município" e "Código de Serviço Federal" podem ser informados na perspectiva de Incidência ou do Emitente, consulte a documentação para mais detalhes: 

NFS-eNFS-eNFS-e

**01. Sobre**: Nesta aba estão os campos para configurar alguns comportamentos específicos do serviço para emissão da NFS-e.

**02. Campos**:

Valor Total Recebido: Indica se o campo vai ser gerado na nota, cujo default é desmarcado.

Não Preencher Grupo de Prestação: Quando marcado remove o grupo <prestacao> da NFS-e, este campo deverá ser marcado somente quando a Incidência do ISS for devido para a origem (Filial emitente).
