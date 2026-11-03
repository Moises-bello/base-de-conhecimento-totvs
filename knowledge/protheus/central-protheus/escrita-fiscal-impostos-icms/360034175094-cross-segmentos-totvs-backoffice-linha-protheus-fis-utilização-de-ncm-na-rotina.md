---
article_id: 360034175094
category: Escrita Fiscal - Impostos - ICMS
content_hash: 56736913084ae524382267ed7a2b2f90fc9a3912248b79fbae0fa4dc418ab87a
fetched_at: '2026-06-28T22:39:26.017666+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Utilização de NCM
  na Rotina UF x UF - FISA080
type: support-article
updated_at: '2021-12-23T14:46:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034175094-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Utiliza%C3%A7%C3%A3o-de-NCM-na-Rotina-UF-x-UF-FISA080
---

**Dúvida**

Utilização de NCM na Rotina UF x UF - FISA080  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Com objetivo de agilizar o cadastro na rotina UFxUF, foi desenvolvido um Facilitador, disponível na opção “Ações Relacionadas” desta rotina. Este facilitador realizará o processamento de cadastro em lote, considerando o filtro e os valores informados pelo usuário por meio das perguntas desta rotina. Abaixo seguem detalhes de preenchimento destas perguntas:

**UF Origem:** Informe a UF de origem que será gravada.

**UF Destino:** Informe a UF de destino que será gravada.

**Importante**

Para considerar todas as UFs como destino, basta informar “\*\*” na pergunta UF Destino.

**NCM De:** Informe a NCM inicial que deseja realizar o processamento;

**NCM Até:** Informe a NCM final que deseja realizar o processamento;

**Importante**

Para considerar todas NCMs, basta deixar a pergunta NCM De com conteúdo vazio e a pergunta NCM Até toda preenchida com letra “Z”.

**Grupo De:** Informe o Grupo de Tributação inicial para o qual deseja realizar o processamento;

**Grupo Até:** Informe o Grupo de Tributação final para o qual deseja realizar o processamento;

**Importante**

Para considerar todos os Grupos de Tributação basta deixar a pergunta Grupo De com conteúdo vazio e a pergunta Grupo Até toda preenchida com letra “Z”.

**Produto De:** Informe o código de produto inicial que deverá ser considerado no processamento;

**Produto Até:** Informe o código do produto final que deverá ser considerado no processamento;

**Importante**

Para considerar todos os Códigos de Produto, basta deixar a pergunta Produto De com conteúdo vazio e a pergunta Produto Até toda preenchida com letra “Z”.

**Edita?:** Por meio desta pergunta será indicado se o processamento do facilitador irá editar ou não um registro, caso ele já exista. Informe as opções disponíveis:

**Sim:** Irá editar registro;

**Não:** Não irá editar registro.

**Origem Produto?:** Por meio desta pergunta será validado qual origem do produto deve ser processado.

Após a confirmação destas perguntas, será exibida uma tela com o seguinte campo:

**- Alíquota do FECP**

Neste campo deverá ser informado o valor da alíquota do FECP, que deverá ser gravado na tabela UFxUF para UF destino/origem, NCM, Grupo de Tributação e Produtos informados nas perguntas anteriores.

O artigo acima refere a tratativa da NCM, para maiores informações sobre a rotina UF x UF, poderá acessar o link abaixo:

<https://tdn.totvs.com/display/public/PROT/CADUF+-+UFxUF>
