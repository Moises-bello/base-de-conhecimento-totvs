---
article_id: 360016771731
category: SIGAACD - Automação e Coleta de Dados
content_hash: 03c65e8b050f73b55059f59a7f5d5776365fc99ba90784af18f3fca761cc6ef7
fetched_at: '2026-06-28T22:39:10.951087+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como configurar o
  ACD para imprimir etiquetas?
type: support-article
updated_at: '2026-02-04T14:37:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016771731-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-configurar-o-ACD-para-imprimir-etiquetas
---

O artigo fornece um guia sobre como configurar o ACD para imprimir etiquetas no sistema TOTVS Backoffice Protheus. A configuração requer uma impressora com linguagens homologadas como ZPL, EPL, DPL ou IPL. O processo envolve o cadastro de locais de impressão na rotina ACDA060, compilação de RDMakes específicos e ajuste de parâmetros principais. A impressão de etiquetas depende de registros na tabela SB2 e saldo no campo B2\_QATU. Não é possível configurar múltiplas filas de impressão automaticamente, mas é sugerido o uso de um servidor spool de impressão. Para soluções personalizadas, recomenda-se o Processo de Desenvolvimento Participativo. Links adicionais fornecem mais informações sobre o ACD e configurações de impressoras.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33684201725719) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como configurar o ACD para imprimir etiquetas?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

### **1 - Possuir uma impressora com uma das Linguagens Homologadas.**

• **ZPL** - Linguagem de programação do fornecedor **Zebra**  
• **EPL** – Linguagem de programação do fornecedor **EPL**  
• **DPL**  – Linguagem de programação do fornecedor **DATAMAX**  
• **IPL**– Linguagem de programação do fornecedor **INTERMEC**  
**Cadastrar os Locais de Impressão na rotina ACDA060,** [**clique aqui**](https://tdn.totvs.com/x/hcKfKw) **e veja um passo a passo;**

### 

### **2 - Compilar um dos RDMakes referente ao Fornecedor da impressora.**

*RDMAK ->ZEBRA*  
*RDMAK ->INTERMEC*  
*RDMAK ->DATAMAX*  
*RDMAK ->ELTRON*

[*https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1152110*](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1152110)

![RDMAKES.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36952898232983)

### **3 - Realizar as configurações nos principais parâmetros. Configurar conforme a sua necessidade.**

**MV\_IACD01** Codigo do tipo de impressao usado no programa expedicao, no modulo ACD, este codigo se refere a tabela CB5.                      
**MV\_IACD02** Codigo do tipo de impressao usado no programa de Pedido de compra e/ou recebimento de materiais este codigo se refere a tabela CB5.                
**MV\_IACD03** Codigo do tipo de impressao usado no programa de Identificacao de produto este codigo se refere a tabela CB5.               
**MV\_IACD04** Codigo do tipo de impressao usado no programa de Identificacao de produto na producao este codigo se refere a tabela CB5.   
Nos parametros acima (*Indicar o código (**CB5\_CODIGO**) da impressora da rotina Locais para Impressão ACDA060)*

**MV\_ACDCB0 -** (01\*02\*03\*04\*05\*06\*07) ([Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14441132913943-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-MV-ACDCB0-quais-op%C3%A7%C3%B5es-dispon%C3%ADveis-no-par%C3%A2metro) e veja FAQ sobre o parâmetro)

**MV\_IMPIP**

**1** - Pedido de Compra   
**2** - Recebimento   
**3**- Não IMPRIME   
**4** - Documento de Entrada.

**Atenção:** A impressão de etiquetas ocorre apenas se o produto tiver registros na tabela SB2 e saldo no campo B2\_QATU.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38160261695767)

No link abaixo temos mais informações sobre os parâmetros do ACD  
[PACD0007 - Parâmetros - Automação e Coleta de Dados (ACD).](http://tdn.totvs.com/pages/releaseview.action?pageId=235596091)

Veja também as instruções e exemplos abaixo de configurações:  
***Impressão Etiquetas via Gerenciador de Impressão***  
[***https://tdn.totvs.com/x/hcKfKw***](https://tdn.totvs.com/x/hcKfKw)

***Como utilizar a impressora virtual Zebra***  
[***https://tdn.totvs.com/x/8IdwLw***](https://tdn.totvs.com/x/8IdwLw)

### **É possível utilizar mais de uma impressora/fila com MscbSpool?**

Atualmente, o padrão do sistema não permite a configuração de múltiplas filas de impressão.

Compartilhamos abaixo o posicionamento oficial da nossa equipe de Produto:

> “Atualmente, não é possível configurar mais de uma impressora por fila no ACD, de forma que o sistema distribua automaticamente as impressões entre as impressoras disponíveis.  
> O método mais próximo dessa funcionalidade seria a implementação de um servidor *spool* de impressão, o qual receberia os comandos de impressão e, dentro deste *spool*, seria possível configurar múltiplas impressoras.  
> No entanto, a escolha da impressora e o comando de envio da impressão ainda ocorreriam de forma manual (via MsCBSpool).  
> Caso haja interesse em uma solução com esse comportamento, sugerimos direcionar a demanda à Fábrica de Software, que já possui experiência com projetos semelhantes.”

Como alternativa, recomendamos a avaliação de um desenvolvimento específico por meio do Processo de Desenvolvimento Participativo (PDP), no qual é possível solicitar ao time de Desenvolvimento a criação de um ponto de entrada personalizado, conforme as necessidades da sua empresa.  
Mais informações sobre esse processo estão disponíveis no seguinte link:  
[Criação de novo Ponto de Entrada – TDN TOTVS](https://tdn.totvs.com/pages/releaseview.action?pageId=589518919)

**Saiba Mais:**

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)  
[*SIGAACD - Quais Coletores de Dados são homologados para uso no módulo Automação e Coleta de Dados (SIGAACD)?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018771512-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Quais-Coletores-de-Dados-s%C3%A3o-homologados-para-uso-no-m%C3%B3dulo-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados-SIGAACD?source=search)  
[*Configurar impressora para impressão de etiquetas*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas)
