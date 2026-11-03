---
content_hash: ee7eda2142dd9356ce0ad6f11ae6725d9dd1aede94a6f7cd982eeec14d9ab07d
fetched_at: '2026-06-29T00:09:13.452681+00:00'
page_id: '420547798'
product: rm
source: tdn-rm
title: Perguntas DCTFWeb
type: documentation
url: https://tdn.totvs.com/display/LRM/Perguntas+DCTFWeb
version: 19
---

**Objetivo:**

---

       Este documento tem como propósito auxiliar no esclarecimento de dúvidas frequentes relacionadas à DCTFWeb, abordando questões comuns e fornecendo orientações para a correta interpretação e utilização do sistema.

---

### 01.Por que o lançamento financeiro da DCTFWeb não possui os mesmos agrupamentos ou quebras da GPS ?

Na GPS, o usuário tinha flexibilidade para definir a forma de quebra dos lançamentos financeiros, incluindo a possibilidade de gerar guias conforme suas próprias definições. Com a implementação da DCTFWeb, o tipo de agrupamento deixou de seguir o mesmo padrão da GPS devido à estrutura do eSocial, sendo agora baseado no retorno do governo, evento S-5011.

Na DCTFWeb, não há o conceito de seção, apenas os de empresa/coligada (em que um único lançamento é gerado), filial e lotação tributária  (no caso de tomador). Assim, o lançamento financeiro tipo "**25 - Total Guia INSS DCTFWeb**" é gerado com base no retorno do S-5011 e nas quebras mencionadas.

Qualquer quebra adicional que venha a ser implementada, diferente da estrutura do eSocial, poderá resultar em diferenças de valores devido ao tipo de agrupamento. Contudo, caso seja necessário visualizar lançamentos específicos por funcionário, basta acessar o cadastro de lançamento financeiro no anexo "Rastreabilidade do Lançamento Financeiro", onde é possível visualizar os valores gerados para cada chapa individualmente.

Lembrando que, o lançamento financeiro deve refletir a geração da DARF, e conforme no documento de perguntas e respostas da DCTFWeb, a DARF deve ser única por estabelecimento. Link <https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/perguntas-e-respostas/dctfweb/perguntas-e-respostas-dctfweb-junho-2024.pdf>

### **02. A conciliação dos valores pagos via DARF Numerada + DARF Avulsa será realizada pela SISTAD? Essa conciliação será exibida no ambiente da DCTFWeb?**

A conciliação será disponibilizada no eCAC, e o cliente precisará apropriar/alocar o DARF Avulso na DCTF. As instruções detalhadas serão comunicadas ainda este mês.

### **03. Paguei o valor disponibilizado pela DCTFWeb, mas precisei reabrir e retificar o período. A DCTFWeb disponibilizará uma DARF apenas com a diferença, incluindo juros e multa? Como devo proceder?**

Sim, a DCTFWeb emitirá uma DARF apenas com a diferença a ser paga. Juros e multa serão aplicados somente se o pagamento ocorrer após a data de vencimento.

### **04. Os valores referentes ao Dissídio Retroativo são pagos na DCTFWeb do mês de pagamento do dissídio ou na competência da Data-Base do dissídio?**

Os valores são considerados no mês de pagamento do dissídio. No exemplo citado, a contribuição previdenciária referente à folha de diferença do dissídio, paga em 08/2018, aparecerá na guia de recolhimento da DCTFWeb referente a 08/2018.

### **05. É possível gerar a DARF para pagamento por filial, ou a DARF é gerada apenas para a empresa MATRIZ?**

A DARF é gerada exclusivamente por empregador, ou seja, apenas para a matriz.

### **06. Não foi possível enviar nenhum evento periódico S-1299 ou S-1295 no prazo, ou seja, não existe nenhuma informação da Folha no eSocial, porém a empresa conseguiu finalizar o REINF. Neste caso, é possível fazer uma DARF avulsa do valor total da Folha de Pagamento/Autônomo e encaminhar no DCTF? A Receita irá reconhecer este pagamento como sendo da minha Folha, mesmo sem a base declaratória, permitindo a retificação posterior do eSocial?**

Sim, caso haja valores do REINF na DCTF, é possível enviá-los e gerar a DARF da DCTF apenas para esses valores. Já os valores relacionados ao eSocial devem ser pagos por meio de uma DARF Avulsa. Posteriormente, ao retificar as informações do eSocial, os valores pagos serão conciliados.

---

**OUTROS LINKS**
