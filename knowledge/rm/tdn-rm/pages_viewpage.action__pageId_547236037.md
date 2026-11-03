---
content_hash: 48d3ee1485a348cf9cda188d6ea5c991e97dcd8b78b492447f04b2c4e0be07b0
fetched_at: '2026-06-29T00:10:42.280095+00:00'
page_id: '547236037'
product: rm
source: tdn-rm
title: Como gerar a correção da dedução do Afastamento Empregado COVID-19 - Norma
  Orientativa 2020.21
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547236037
version: 12
---

Conforme a Nota Orientativa 2020.21, a Lei nº 13.982 de 02 de abril de 2020, artigo 5º, autoriza as empresas a deduzirem de suas contribuições devidas à previdência social os valores pagos em relação aos 15 primeiros dias de salário do trabalhador afastado por enfermidade causada pelo Covid-19.

Para atender NO 2020.21 foram liberados os códigos de cálculos **436-ATESTADO MÉDICO DE AFASTAMENTO POR COVID-19** e **437-DIFERENÇA DE ATESTADO MÉDICO POR COVID-19** conforme orientações no [link](https://tdn.totvs.com/display/LRM/NO+2020.21+-+Afastamento+Empregado+Covid-19).

Porém houve a necessidade de realizar uma modificação na geração do evento S-1010 para que na tag<TpRubr> seja levado **"3-Informativa"** ao invés de ser levado **"4-Informativa Dedutora"**, com isso ocorrerá a dedução do valor desta rubrica na DCTFWeb, conforme orientação do governo.

Para isso liberamos os patchs **12.1.25.271, 12.1.26.217, 12.1.27.173 e 12.1.28.107.**

Como gerar a correção da dedução do Afast

Caso o usuário tenha enviado o evento S-1010 - Tabela de Rubricas desta verbas e/ou o evento "S-1200-Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social" antes destes patchs se faz necessário realizar a retificação destes eventos. Segue abaixo passo a passo para essa retificação:

Acesse o menu eSocial | Fila de Eventos

Clique em <Incluir>

Cadastre um gatilho de alteração do evento S-1010 para as verbas com o código de calculo 436 e código de cálculo 437, selecione a mesma competência em que foi enviado o seu evento e cadastre o tipo da Operação - Alteração;

Gere o xml's e envie ao RET.

Abaixo, segue um exemplo abaixo de como ficará o xml com a tag <tpRubr> 3 - Informativa.

Após o aceite do governo das rubricas, acesse o menu eSocial | Eventos Periódicos

Selecione qual(is) funcionário(s) deseja retificar, e acesse o Processos | Gerar Retificação Arquivo eSocial

Será gerado na fila um gatilho de retificação para os funcionários selecionados, gere o xml e envie ao RET.

**Observação:**

Caso já tenha sido enviado o evento "S-1210 - Pagamentos de Rendimentos do Trabalho", deverá enviar a exclusão antes da retificação do evento  "S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social".
