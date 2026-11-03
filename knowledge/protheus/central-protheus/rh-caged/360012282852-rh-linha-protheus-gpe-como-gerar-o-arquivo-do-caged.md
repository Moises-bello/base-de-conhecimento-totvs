---
article_id: 360012282852
category: RH - CAGED
content_hash: c9a8b937bce87c5107f4d1fe0fe02814a56a5b23f6327f46cafe13394402ddeb
fetched_at: '2026-06-28T22:43:33.058701+00:00'
product: protheus
section_id: 360010781674
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar o arquivo do CAGED
type: support-article
updated_at: '2025-08-27T20:34:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012282852-RH-Linha-Protheus-GPE-Como-gerar-o-arquivo-do-CAGED
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29401077873559) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como gerar o arquivo do CAGED?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**O **CAGED** - Cadastro Geral de Empregados e Desempregados, é gerado pelas empresas que possuem funcionários admitidos e/ou demitidos, num período mensal, sendo que a data de entrega obedece ao estabelecido pelo MTE - Ministério do Trabalho e Emprego, conforme base legal.  
  
Esta rotina gera um arquivo com o nome de **CGDE** + Ano + .M + mês de referência. Tal arquivo deve ser submetido ao validador do MTE - Ministério do Trabalho e Emprego.  
  
Para acessar essa funcionalidade, clique em: **GPEM400**- **Miscelânea/CAGED/Arquivo Magnético:**

![](http://tdn.totvs.com/download/attachments/233734786/1.JPG?version=2&modificationDate=1457525285000&api=v2 "Linha Microsiga Protheus > PSIGAGPE0367 - GPEM400 - Como gerar o arquivo do CAGED? > 1.JPG")

![](http://tdn.totvs.com/download/attachments/233734786/caged2.JPG?version=2&modificationDate=1457525287000&api=v2 "Linha Microsiga Protheus > PSIGAGPE0367 - GPEM400 - Como gerar o arquivo do CAGED? > caged2.JPG")![](http://tdn.totvs.com/download/attachments/233734786/caged3.JPG?version=3&modificationDate=1457525288000&api=v2 "Linha Microsiga Protheus > PSIGAGPE0367 - GPEM400 - Como gerar o arquivo do CAGED? > caged3.JPG")![](http://tdn.totvs.com/download/attachments/233734786/caged4.JPG?version=2&modificationDate=1457525289000&api=v2 "Linha Microsiga Protheus > PSIGAGPE0367 - GPEM400 - Como gerar o arquivo do CAGED? > caged4.JPG")![](http://tdn.totvs.com/download/attachments/233734786/caged5.JPG?version=2&modificationDate=1457525290000&api=v2 "Linha Microsiga Protheus > PSIGAGPE0367 - GPEM400 - Como gerar o arquivo do CAGED? > caged5.JPG")  
  
**Observações sobre algumas perguntas para geração do CAGED:**  
  
**- 1ª Declaração:** Neste campo selecione SIM apenas se for a primeira entrega da declaração.

**- Versão do Caged?:** Selecione entre a versão Atual ou a Anterior para validação das informações. Importante: Utiliza-se a versão Anterior quando a entrega se é referente a versão anterior.

- **Gerar CAGED por?:** Selecione entre Filial ou Centro de Custo.

- **Tipo de Correção?:** Selecione entre Inclusão ou Exclusão.

- **Verbas que compõem Remunerac.?:** Preencher com as Verbas do Acumulado Anual a serem incorporadas ao Salário.  
Ex.: Para incorporar as Verbas 123 e 124 preencher com 123124.  
- **Grupo Verbas comp. Remunerac.?:** Selecione o grupo de verbas do acumulado que serão incorporadas ao salário. A definição de grupos é feita através do campo **'RV\_GRPVERB'** no cadastro de Verbas.

- **Porte do Estabelecimento?:** Informe se o porte da empresa é:  
1- Micro Empresa;  
2- Empresa de pequeno porte;  
3- Empresa/Órgão não classificado nos itens anteriores.

- **Tipo do Salário?:** Informe se deseja gerar o salário pela remuneração recebida ou pelo salário contratual **(RA\_SALARIO).   
  
Importante:** É possível selecionar grupos de verbas do Acumulado Anual que serão incorporadas ao salário do funcionário no arquivo do CAGED.  
Caso o período de referência da geração seja o mesmo da Folha de Pagamento em aberto para cálculo, as verbas serão pesquisadas nos Lançamentos Mensais.

**Saiba Mais**Para adquirir mais informações acesse o *link*:  
[MP - GPE0367 - GPEM400: Como gerar o arquivo do CAGED?](http://tdn.totvs.com/pages/viewpage.action?pageId=233734786)  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)

Essas documentações também podem ser acessadas através da Carolina, veja como acessar a assistente virtual, via Protheus ou central de atendimento:   
<https://www.youtube.com/watch?v=T7b4zMlphTI>
