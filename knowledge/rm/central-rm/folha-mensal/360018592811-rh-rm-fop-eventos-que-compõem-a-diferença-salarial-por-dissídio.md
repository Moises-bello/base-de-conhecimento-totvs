---
article_id: 360018592811
category: Folha Mensal
content_hash: 0913f9f505c6fb458ff640988a19ed3bd01dc2502050e3fd99d28c1fe61f4953
fetched_at: '2026-06-28T22:47:00.211303+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Eventos que compõem a diferença salarial por dissídio
type: support-article
updated_at: '2024-09-16T20:06:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018592811-RH-RM-FOP-Eventos-que-comp%C3%B5em-a-diferen%C3%A7a-salarial-por-diss%C3%ADdio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:07min 12sec****Dúvida**Quais os eventos que compõem a diferença salarial por dissídio?  **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
 **Solução**Para realizar a parametrização correta que torna possível a utilização da diferença salarial por dissídio, os eventos abaixo devem estar cadastrados. Acesse: **Administração de Pessoal | Eventos | Eventos** e confira o cadastro:  
  
1. Evento - **Diferença salarial** - [Código de Cálculo 37 -](https://tdn.totvs.com/pages/releaseview.action?pageId=452718613) **Provento** - **Tipo valor** - **tem** incidência em INSS.  
  
No caso de aumento salarial dentro do mesmo mês, o sistema deduzirá do salário novo o que já foi pago e lançará a diferença neste evento. Os eventos do tipo hora serão recalculados e a diferença adicionada a este evento.  
  
No caso de dissídio, deverá cadastrar um evento com Código de Cálculo 37 – com as mesmas incidências, **exceto em INSS**, conforme será demonstrado no próximo item.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8905212079767/mceclip0.png)  
  
Incidência em INSS marcada.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8905213580695/mceclip1.png)  
  
2. Evento - **Diferença salarial** -  [Código de Cálculo 37 -](https://tdn.totvs.com/pages/releaseview.action?pageId=452718613) **Provento** - **Tipo valor** - **não** **tem** incidência em INSS.  
  
No caso de aumento salarial em meses anteriores à competência atual, o sistema calculará proporcionalmente todos os meses onde o salário deveria ser conforme o aumento, fará a diferença do que foi pago em relação ao novo salário e lançará esta diferença neste evento.   
  
Este evento não pode ter incidência em INSS, pois como o recolhimento de INSS é por competência, o valor de INSS resultante desta diferença deverá ser recolhido pela SEFIP 650.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8905203096855/mceclip2.png)  
  
Não possui incidência em INSS marcada.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8905254796695/mceclip3.png)

3. Evento - **Diferença de vale transporte** -  [Código de Cálculo 64 -](https://tdn.totvs.com/pages/releaseview.action?pageId=452718637) **Desconto** - **Tipo valor**O sistema fará o acerto do desconto de vale-transporte do funcionário que tiver aumentos retroativos a semanas já liberadas e que deve ter o vale descontado sobre o salário atual.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8905257269271/mceclip4.png)

4. Evento - **Diferença salário família** - [Código de Cálculo 65 -](https://tdn.totvs.com/pages/releaseview.action?pageId=452718611) **Provento ou Desconto**, **ambos Tipo Valor**Permite o lançamento de eventuais acertos de salário família. O evento que tiver este código de cálculo poderá ser cadastrado como um provento ou como um desconto: provento do tipo valor incidindo no líquido ou desconto do tipo valor também incidindo no líquido. O sistema calculará automaticamente a diferença de salário família quando houver uma alteração no "Valor Fixo do Salário Família" e o usuário deverá cadastrar o evento de diferença no evento de Código de Cálculo 5 - Salário Família.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098026634/mceclip4.png)

5. Evento - **INSS diferença salarial** - [Código de Cálculo 68 -](https://tdn.totvs.com/pages/releaseview.action?pageId=452718219) **Desconto** - **Tipo valor**Este código de cálculo será utilizado para o desconto do INSS referente ao evento de diferença salarial quando for no caso de dissídio coletivo e será calculado de acordo com a tabela de INSS dos meses dos referidos aumentos salariais.  
  
**Exemplo:**A Empresa X está no mês competência Jan/2001 e tem o dissídio coletivo retroativo a Set/2000 o sistema calculará as diferenças salariais, quando for marcado no cálculo da diferença salarial que é referente ao dissídio, refazendo a base de cálculo de INSS de cada mês e buscando na tabela o percentual de incidência atualizado.  
  
**Importante**INSS Diferença Salarial, utilizado também para diferença Rescisão Complementar, se for processar uma diferença salarial, logo após calcular uma rescisão complementar, no mesmo período, terá que marcar a opção de “Adicionar Valor” e não “Substituir Valor”.  
  
Como o SEFIP 650/655 não é distribuído por tomador, o evento com código de cálculo igual a 68 sempre é distribuído para o tomador empresa.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8905297847703/mceclip7.png)  
  
6. Evento - **Base de FGTS de diferença salarial** - [Código de Cálculo 69 -](https://tdn.totvs.com/pages/releaseview.action?pageId=452719698) **Base de cálculo** - **Tipo valor** - **Não** tem incidências.  
  
Base de cálculo do tipo valor. Este código de cálculo será utilizado para informação do total pago de diferença salarial referente dissídio coletivo. Este valor não compõe a base de cálculo do INSS do mês porque já existe calculado sobre este valor o INSS diferença salarial.  
  
**Importante**A diferença do Aviso Prévio Indenizado sempre será acumulada no Código de Cálculo 69 para que o valor saia na GRRF. No SEFIP será tratado para que o valor do [Código de Cálculo 99](https://tdn.totvs.com/pages/releaseview.action?pageId=452718356) não seja considerado novamente, e assim duplicar o recolhimento.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8905300688663/mceclip8.png)  
  
7. Evento - **Estorno Base INSS Dissidio Ret. Folha** - [Código de Cálculo 114 -](https://tdn.totvs.com/pages/releaseview.action?pageId=452718664) **Base de cálculo - Tipo Valor** - Incidência em **Estorno INSS** de folha.  
  
Este evento será utilizado para o cálculo de diferença referente a dissídio. Este evento será o somatório da diferença calculada dos eventos pagos, que tenham incidência em INSS folha. Deve incidir no estorno de INSS.  
  
**Exemplo:**Dias Trabalhados.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8905333092503/mceclip9.png)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8905334688407/mceclip10.png)

8. Evento - **Diferença De Pensão Alimentícia Folha** - [Código de Cálculo 195 -](https://tdn.totvs.com/pages/releaseview.action?pageId=452718414) **Desconto** - **Tipo valor** - Incidência **Dedutível IRRF** de folha.  
  
Este evento permite a utilização de fórmulas para o cálculo.  
  
**Importante**Este código de cálculo será lançado automaticamente no movimento do funcionário quando houver cálculo de diferença salarial e no movimento do funcionário a ser calculada a diferença, existir o [Código de Cálculo 13](https://tdn.totvs.com/pages/releaseview.action?pageId=452718801) - Pensão Alimentícia de Folha.  
  
Será gerado um movimento de pensão para o dependente como Dif. de Movimento (Movimento = 4) e registrado no cadastro do dependente (**Cadastros | Funcionários | Base de Cálculo | Dependentes | pasta Movimento da Pensão**).

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8905389199127/mceclip11.png)

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8905390402327/mceclip12.png)
