---
article_id: 4412006921751
category: Rescisão
content_hash: 98a75b5387dc4ba751a7559fd3f779f021800cdab2749376f5a4e2b9f5b96791
fetched_at: '2026-06-28T22:46:54.479330+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: RH - RM - FOP - Antecipação de contrato por prazo determinado sem cláusula
  assecuratória
type: support-article
updated_at: '2025-01-20T21:54:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412006921751-RH-RM-FOP-Antecipa%C3%A7%C3%A3o-de-contrato-por-prazo-determinado-sem-cl%C3%A1usula-assecurat%C3%B3ria
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como realizar antecipação de contrato por prazo determinado, de modo que leve as informações de aviso corretamente para a GRRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar a antecipação de contrato por prazo determinado, será necessário atentar-se às  parametrizações realizadas no ato do preenchimento do cadastro do colaborador, especialmente no item **Registro**, na aba **Dados do Contrato**. Portanto, realize os passos abaixo:  
  
1. Acesse o cadastro do colaborador e preencha os dados do contrato de admissão do funcionário.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411995263255/mceclip1.png)  
  
2. Na aba **Dados do Contrato**, preencha as informações do contrato e informe se possui ou não a cláusula assecuratória. Para isso, deve-se realizar a marcação ou não da flag **Contém cláusula assecuratória.**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411988283287/mceclip3.png)  
  
3. Na aba **Rais** informe o tipo de contrato no campo **Vínculo da Rais** corretamente, para não haver conflito de informações no tipo de contrato na geração do Termo de Rescisão de Contrato de Trabalho.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411995521943/mceclip4.png)  
  
3. Após conferir as informações, realize a rescisão do colaborador.  
  
**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411995644439/mceclip5.png)**4. O tipo de rescisão será tipo 2- Iniciativa do Empregador.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411995683735/mceclip6.png)  
  
5. Após cálculo da rescisão, no envelope do colaborador, serão lançadas as verbas devidas e a indenização do artigo 479.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411997222807/mceclip7.png)

**Quanto ao processo da GRRF:**  
  
1**.** Ao gerar a GRRF será levado o tipo de aviso 3, correspondente ao tipo de rescisão por antecipação de contrato e iniciativa do colaborador, para que seja validado na GRRF da caixa.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411996233879/mceclip9.png)  
  
Observe exemplo abaixo, apresentando o Tipo de aviso 3.  
  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412000069271/mceclip13.png)  
  
2. Nos parâmetros específicos da coligada, informe a chapa do colaborador, caso gere apenas uma chapa.  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411997561367/mceclip10.png)  
  
3. Após a geração  GRRF da Caixa, virão as informações pertinentes ao tipo de rescisão, informando o tipo de aviso 3-  ausência / dispensa.  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411998423703/mceclip11.png) **Importante**No sindicato, há um parâmetro para que seja informada uma fórmula de valor, onde não há a obrigatoriedade de pagamento, retornará valor zerado.  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411998708503/mceclip12.png)

**Saiba Mais**[RH - RM - FOP - Diferença dos contratos por prazo determinado com e sem cláusula assecuratória](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034184533-RM-FOP-Diferen%C3%A7a-dos-contratos-por-prazo-determinado-com-e-sem-cl%C3%A1usula-assecurat%C3%B3ria?source=search)  
[Como pagar o artigo 479 na rescisão?](https://tdn.totvs.com/pages/releaseview.action?pageId=155582702)
