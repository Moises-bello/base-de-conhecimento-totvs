---
article_id: 360017598352
category: Rescisão
content_hash: ebf913e2893615f3549f18202433eab78203db1cefc45a65a9e9004bba755ef3
fetched_at: '2026-06-28T22:46:55.375637+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: Como lançar a indenização do artigo 480?'
type: support-article
updated_at: '2025-09-03T17:05:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017598352-RH-RM-FOP-Rescis%C3%A3o-Como-lan%C3%A7ar-a-indeniza%C3%A7%C3%A3o-do-artigo-480
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24131598045975)Tempo aproximado para leitura:00:05:20 min  
  
Dúvida**Como realizar o desconto da indenização a que trata o Artigo 480?  
  
Art. 480  
Havendo termo estipulado, o empregado não se poderá desligar do contrato, sem justa causa, sob pena de ser obrigado a indenizar o empregador dos prejuízos que desse fato lhe resultarem.  
  
§ 1º A indenização, porém, não poderá exceder àquela a que teria direito o empregado em idênticas condições. Nota: Renumerado pelo Decreto-lei nº 6.353/44  
  
§ 2° Em se tratando de contrato de artistas de teatros e congêneres, o empregado que rescindi-lo sem justa causa não poderá trabalhar em outra empresa de teatro ou congênere, salvo quando receber atestado liberatório, durante o prazo de um ano, sob pena de ficar o novo empresário obrigado a pagar ao anterior uma indenização correspondente a dois anos do salário estipulado no contrato rescindido.  
  
**Ambiente**RM - Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar o lançamento da indenização do artigo 480, siga os passos abaixo:  
  
**01.** Acesse **Administração de Pessoal | Fórmulas** e crie as seguintes fórmulas:  
  
Código: ART480  
Título: Indenização Artigo 480  
Texto: ((RC/30) \* (DTD - TABFUNC('FIMPRAZOCONTR','D')))/2  
**\*** A fórmula pode ser adaptada para considerar outras remunerações desejadas. No formato atual a fórmula considera somente o salário de contrato do funcionário.  
  
Código: ART480SE  
Título: Seleção para Indenização Artigo 480  
Texto: SE TABFUNC ('TIPODEMISSAO', 'S')='4' E TABFUNC('FIMPRAZOCONTR','D')>DTD ENTAO 1 SENAO 0 FIMSE  
***\**** Marcar o flag "Fórmula de seleção".  
  
**02.** Acesse **Administração de Pessoal | Eventos** e crie um novo evento do tipo Desconto/Valor, sem código de cálculo e informe a fórmula ART480 no campo **Fórmula Valor**;  
  
**03.**Acesse **Configuração | Parametrizador| Rescisão** e acesse a aba **Parâmetros de Rescisão | Eventos Adicionais**. Insira o evento criado no passo anterior (2). Caso ele não apareça aperte "CTRL + R") e no campo "Fórmula de seleção" informe a fórmula ART480SE.  
  
**04.** Acesse o cadastro de rescisãoeinforme os dados para o cálculo da demissão do funcionário. O campo **Contrato com prazo** deve estar marcado e a data informada corretamente.  
  
  
**Observação:**O tipo da demissão deve ser do tipo **4 - Inic. Empregado sem justa causa**.O tipo de rescisão **T** deve ser utilizado somente quando a data de demissão for exatamente o dia de término do contrato.
