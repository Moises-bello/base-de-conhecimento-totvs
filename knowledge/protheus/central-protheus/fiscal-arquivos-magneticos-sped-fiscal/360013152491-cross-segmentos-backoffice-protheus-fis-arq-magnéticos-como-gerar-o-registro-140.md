---
article_id: 360013152491
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: bdab27eaeb56644657c08bd36801a06d29c686921376099c67526228518131aa
fetched_at: '2026-06-28T22:42:00.919486+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como Gerar
  o Registro 1400
type: support-article
updated_at: '2025-02-11T20:58:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013152491-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-Gerar-o-Registro-1400
---

**Dúvida**Como gerar o registro 1400 do SPED FISCAL.  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
**REGISTRO 1400: Informação sobre valores agregados**Gera-se este registro a partir dos Livros Fiscais, no cadastro dos tipos de entrada e Saída, com o preenchimento do campo **Agr. Vlr. Mun.** (Valores agregados por Município - **F4\_VLAGREG**) e com os valores S=Soma ou D=Deduz.   
O**MV\_ESTADO** deve ser o mesmo do cliente ou fornecedor, dependendo da operação. Se as Notas Fiscais forem geradas pelo módulo TMS, o código do município informado no registro será o do início da prestação do serviço (Origem).   
Esse registro pode ser gerado manualmente, através do ponto de entrada **SPED1400.** O processo realizado através do Ponto de Entrada, deve seguir as mesmas configurações da TES, informados acima**.**

Link referente o ponto de entrada **SPED1400**:

<https://tdn.totvs.com/pages/releaseview.action?pageId=706922994>

1. Para geração do registro 1400, configure o TES conforme os campos abaixo:  
  
![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2017%3A41%3A2.png?version=1&modificationDate=1465155309000&api=v2)  
  
Código da Situação tributária do ICMS **(F4\_SITTRIB);**Código da Situação tributária do IPI **(F4\_CTIPI);**Código da Situação tributária do PIS, caso seja um TES que calcule PIS**(F4\_CSTPIS);**Código da Situação tributária do COFINS, caso seja um TES que calcule COFINS **(F4\_CSTCOF);**Campo **Agr. Vlr. Mun. (F4\_VLAGREG)** que identifica as informações para o cálculo do valor agregado por Município.  
  
Importante: Para todos os registros no qual é necessário informar a classificação fiscal do item, com relação aos impostos (ICMS, IPI, PIS e COFINS), existe a possibilidade de alterar a classificação fiscal padrão apresentada pelo sistema (composta pelo produto e pelo TES).   
Caso exista esta necessidade, deve-se customizar o **Ponto de Entrada SPDFIS03.** Para mais detalhes sobre este Ponto de Entrada.  
  
2. Configure a pergunta da WIZARD **SPED FISCAL** para geração do registro **1400**.  
  
![](http://tdn.totvs.com/download/attachments/238035285/image2016-6-5%2017%3A41%3A43.png?version=1&modificationDate=1465155352000&api=v2)  
  
**Importante**   
Para geração do registro **1400**, foi disponibilizada no cadastro de TES **(MATA080)** uma nova aba (**í****ndice de Participação dos Municípios**),onde será possível fazer relacionamento do TES com código de IPM e seu respectivo Estado, sem a necessidade de criar um novo campo para cada Estado.   
Essas informações de relação do código IPM e TES ficaram gravadas na tabela **F09**relacionamento TES x IPM**.**3. Informe no parâmetro **MV\_UFIPM** o Estado (s) onde existe código IPM disponibilizado pela SEFAZ, e que o PVA já esteja preparado para fazer validação deste código;  
  
4. Faça a importação/cadastro do código IPM, através da rotinaCódigo da Tabela IPM (**FISA094**);

[CADSPED - Importação da Tabela IPM (Índice de Participação dos Municípios)](https://tdn.totvs.com/pages/viewpage.action?pageId=640901474)

5. Informe o código de IPM no cadastro de TES, através da aba **Índice de Participação dos Municípios.**Esta aba somente será exibida se o parâmetro **MV\_UFIPM** estiver preenchido;  
  
6. Processe o SPED Fiscal;  
  
7. O arquivo magnético será gerado com o registro 1400 e código de IPM informado no TES.  
  
Esse é um tratamento genérico, irá funcionar para todos os Estados, porém o PVA ainda não está pronto para fazer a validação do código IPM de todos os Estados. A medida que o projeto SPED for evoluindo e novos Estados passarem a exigir o código IPM, basta fazer os procedimentos acima que o registro 1400 será gerado automaticamente com informação de IPM, sem necessidade de alteração de programa ou abertura de chamado.

Os campos **F4\_IPMSP** (São Paulo) e **F4\_IPMMG** (Minas Gerais) serão mantidos como legado, pois foram criados antes deste mecanismo genérico, caso não exista informação na aba **Índice de Participação dos Municípios**para esses estados, a rotina continuará buscando informação nesses campos para estados de São Paulo e Minas Gerais.

Caso a Tabela IPM não esteja disponível para o seu Estado, será gravado o código do Item (**FT\_PRODUTO**) conforme orientação do Guia Prático Versão 2.0.15.

**Importante**Para atender a resolução Nº 4.746 do estado de Minas Gerais, deverá ser informado no cadastro de **Índice de Participação de Municípios** **(FISA094)**, o tipo de periodicidade do código (campo **CLN\_TIPO**) informando se o mesmo é anual ou mensal, pois o código "prestação de serviço de transporte rodoviário" deve ser gerado no mês de Dezembro contendo o valor total de todo o exercício para cada município inclusive o município sede.
