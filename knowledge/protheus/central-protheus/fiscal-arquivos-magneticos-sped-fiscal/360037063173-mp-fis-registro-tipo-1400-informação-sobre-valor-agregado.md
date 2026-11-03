---
article_id: 360037063173
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: b8e6d89b1780c85d99e641199494f4669a722802d7836f6b0f1627b0178c23d4
fetched_at: '2026-06-28T22:42:03.816635+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - Registro tipo 1400 - Informação sobre Valor Agregado
type: support-article
updated_at: '2023-11-22T11:23:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037063173-MP-FIS-Registro-tipo-1400-Informa%C3%A7%C3%A3o-sobre-Valor-Agregado
---

**Dúvida**Registro tipo 1400 - Informação sobre Valor Agregado  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Gera-se este registro a partir dos **Livros Fiscais**, no **Cadastro dos Tipos de Entrada e Saída**, com o preenchimento do campo **Agr. Vlr. Mun**. (**Valores agregados por Município - F4\_VLAGREG**) com os valores S=Soma ou D=Deduz. O **MV\_ESTADO** deve ser o mesmo do Cliente ou Fornecedor, dependendo da operação. Se as Notas Fiscais forem geradas pelo módulo **TMS**, o código do município informado no registro será o do início da prestação do serviço (Origem). Esse registro também pode ser gerado manualmente através do ponto de entrada **SPED1400**, o processo feito através do Ponto de Entrada deve seguir as mesmas configurações da TES, informados acima.

Link referente o ponto de entrada **SPED1400**:

<https://tdn.totvs.com/pages/releaseview.action?pageId=706922994>

**Importante** 

Para geração do registro 1400, foi disponibilizada no cadastro de TES ***(MATA080)*** uma nova aba, ***Índice de Participação dos Municípios,***onde será possível fazer relacionamento do TES com código de IPM e seu respectivo Estado, sem a necessidade de criar um novo campo para cada Estado. Estas informações de relação do código IPM e TES ficaram gravadas na tabela ***F09 Relacionamento TES x IPM.***

Para gerar código de IPM no registro 1400 deverá:

1.      Informar no parâmetro ***MV\_UFIPM*** o Estado(s) onde existe código IPM disponibilizado pela SEFAZ, e que o PVA já esteja preparado para fazer validação deste código;

***2.***Realizar importação/cadastro do código IPM através da rotina [CADSPED - Importação da Tabela IPM (Índice de Participação dos Municípios)](https://tdn.totvs.com/pages/viewpage.action?pageId=640901474)

***3.***Informar o código de IPM no cadastro de TES, através da aba ***Índice de Participação dos Municípios.***Esta aba somente será exibida se o parâmetro ***MV\_UFIPM*** estiver preenchido***;***

Desta maneira ao processar SPED Fiscal, o registro 1400 será gerado com código de IPM informado no TES.

Este é um tratamento genérico, irá funcionar para todos os Estados, porém o PVA ainda não está pronto para fazer validação do código IPM de todos os Estados. A medida que o projeto SPED for evoluindo e novos Estados passarem a exigir o código IPM, basta fazer os procedimentos acima que o registro 1400 será gerado automaticamente com informação de IPM, sem necessidade de alteração de programa ou abertura de chamado.

Os campos ***F4\_IPMSP (São Paulo)*** e ***F4\_IPMMG (Minas Gerais)*** serão mantidos como legado, pois foram criados antes deste mecanismo genérico, caso não exista informação na aba ***Índice de Participação dos Municípios***para estes Estados, a rotina continuará buscando informação nestes campos para estados de São Paulo e Minas Gerais.

Caso a Tabela IPM não esteja disponível para o seu Estado, será gravado o código do Item (**FT\_PRODUTO**) conforme orientação do Guia Prático Versão 2.0.15.

**Importante**

Para atender a resolução Nº 4.746 do estado de Minas Gerais, deverá ser informado no cadastro de Índice de Participação de Municípios (FISA094), o tipo de periodicidade do código (campo CLN\_TIPO) informando se o mesmo é anual ou mensal, pois o código "*prestação de serviço de transporte rodoviário*" deve ser gerado no mês de Dezembro contendo o valor total de todo o exercício para cada município inclusive o município sede.
