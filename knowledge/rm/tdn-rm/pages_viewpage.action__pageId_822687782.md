---
content_hash: 12fd77aa23685614c5b063b36538e126bcd16790e337231c80428f04570f3df7
fetched_at: '2026-06-29T00:11:46.488324+00:00'
page_id: '822687782'
product: rm
source: tdn-rm
title: obra/end
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822687782
version: 11
---

As informações do grupo "end" da NFS-e serão geradas ao vincular um projeto no movimento ou no item da nota. Para habilitar o vínculo do projeto, acesse *Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > Etapa 72 - Projeto > Informa Projeto/Tarefa*.

obs.: o Grupo endExt só será gerado para Projetos com enderço onde o "Estado" não esteja marcado com a flag "Nacional".

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| **end** |  | **G** | **1-1** | **Grupo de informações do endereço da obra.** |  | **O Grupo será preenchido conforme informações do Projeto, que pode ser informado no movimento ou no Item do movimento.** |
| CEP | end | E | 1-1 | Código de Endereçamento Postal numérico do endereço nacional da obra. | MPRJ.CEP |  |
| xLgr | end | E | 1-1 | Tipo e nome do logradouro do endereço da obra. | MPRJ.RUA |  |
| nro | end | E | 1-1 | Número no logradouro do endereço da obra. | MPRJ.NUMERO |  |
| xCpl | end | E | 0-1 | Complemento do endereço da obra. | MPRJ.COMPLEMENTO |  |
| xBairro | end | E | 1-1 | Bairro do endereço da obra. | MPRJ.BAIRRO |  |
| **endExt** | **DPS/infDPS/serv/obra/end** | **G** | **1-1** | **Grupo de informações descritivas do endereço da obra no exterior.** |  | **O grupo será preenchido sempre que o país for diferente de Brasil** |
| cEndPost | endExt | E | 1-1 | Código de Endereçamento Postal alfanumérico do endereço no exterior da obra. | MPRJ.CEP |  |
| xCidade | endExt | E | 1-1 | Nome da cidade no exterior, local da obra. | MPRJ.CIDADE |  |
| xEstProvReg | endExt | E | 1-1 | Estado, província ou região da cidade no exterior, local da obra. | MPRJ.UF |  |

Para geração deste grupo, a flag "Gerar Endereço do Projeto" deve estar marcada nos "Dados Fiscais do Município":
