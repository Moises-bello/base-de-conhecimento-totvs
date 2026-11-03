---
article_id: 360017502872
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: e61439c9c76e3a0beb08215b222b05263a3521a779f9b8b56d9ac5e0f3ef0c94
fetched_at: '2026-06-28T22:42:07.765017+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Extrator Fiscal
  - Duplicidade de registro layout T013
type: support-article
updated_at: '2022-08-18T17:23:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017502872-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Extrator-Fiscal-Duplicidade-de-registro-layout-T013
---

**Dúvida**

Como corrigir o erro de Duplicidade no layout T013 no TAF?

**Ambiente**

TAF - A partir de 12.1.17

**Solução**

Esse erro pode ocorrer em algumas situações:

1 - Divergências de tamanho de campo;

2 - Layout T013 ou algum layout filho do T013 gerado duplicado;

3 - Perda do sequencial do Controle de Numeração.

Avaliar as etapas a seguir:

**1 - Divergência de tamanho de campo:**

Atualmente o Extrator Fiscal gera o item da nota (layout T015) com 4 dígitos. O TAF precisou ser adequado e os campos relacionados ao item da nota também precisam estar com tamanho 4. Se por exemplo, um dos campos a seguir, **C30\_NUMITE** ou **C35\_NUMITE** estiver com tamanho 3, é necessário executar a atualização e **UPDDISTR** com dicionário do **TAF**.

[MP - TAF - REINF - Atualização Completa REINF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026673572-MP-TAF-REINF-Atualiza%C3%A7%C3%A3o-Completa-REINF?source=search)

**2 - Layout T013 ou algum layout filho do T013 gerado duplicado.**

Caso os campos estejam com o tamanho correto, avaliar se no TXT do layout T013 alguma linha de um layout filho está duplicado, por exemplo:

|T013|0|01|0|C05748202|00|001||055566|20200303|35200352514627000164550010000555661005558115|1112,00|2|0,00|55|055566|113010001|0,00|20200303|0,00|||||9|0,00|0,00|0,00|9|0,00||||||||1112,00|||||||||||||||||||||||||||||||SP||  
**|T013AP|05|0|0|0|0|0|0|1112|0|01|1949|0||1112|0|0|**  
**|T013AP|05|0|0|0|0|0|0|1112|0|01|1949|0||1112|0|0|**  
|T013AP|06|0|0|0|0|0|0|0|0|98|1949|0||1112|0|0|  
|T013AP|07|0|0|0|0|0|0|0|0|98|1949|0||1112|0|0|  
|T015|0001|0326680049|PRODUTOTESTE|1112,00|0,00||0|113010001|60005|1,00|PC|1949|123|0||0,00|1,00|0,00|||1,00|0,00|0,00|0,00|0,00|0,00|0|1||1112,00||||1112,00||0,00|0,00||||||||  
|T015AE|05|01||0|0|0|0|0|0|0|0|0||0|1112|0|0|0|||0||0|0|0|0|0|0|0|  
|T015AE|06|98||0|0|0|0|0|0|0|0|0||0|0|0|0|0|||0||0|0|0|0|0|0|0|  
|T015AE|07|98||0|0|0|0|0|0|0|0|0||0|0|0|0|0|||0||0|0|0|0|0|0|0|

Neste exemplo de nota fiscal, o layout T013AP possui duas linhas duplicadas. Esse tipo de situação pode ocasionar erro de duplicidade. Caso não seja possível efetuar essa análise, abrir um chamado com a equipe de suporte anexando o TXT gerado pelo extrator fiscal que causou a duplicidade.

**3 - Perda do sequencial do Controle de Numeração.**

Segue abaixo passo a passo para correção do sequencial da tabela C20:

**Controle via License Server:**

Inserir a rotina no menu: Rotina APCFG110  
Esta rotina precisa ser inserida manualmente no menu do Configurador. Ao executá-la, são exibidas a numeração atual e a próxima numeração das tabelas, podendo ser editada essa informação para corrigir a sequência. Para inserir no menu, realize o procedimento a seguir:

1. Acesse o Configurador > Ambiente > Cadastros > Menu

2. Selecione somente o menu do Configurador, e clique em OK

3. Adicione o menu para a coluna Novo Menu

4. Selecione a pasta onde deverá ser criada a nova rotina

5. Clique em Novo Item

6. Preencha o nome que deseja para a rotina no menu

7. Em Programa digite APCFG110

8. Em Módulo selecione Configurador, e clique em OK

9. Clique em Gerar, e selecione o nome para o menu (para manter o padrão, digite SIGACFG)

10. Clique em Gerar

11. Após criado o item de menu, saia do Configurador e entre novamente para visualizar a nova rotina

Após ter criado a rotina no menu, acesse-a e siga os passos abaixo para acertar a numeração:

1. Acesse a rotina APCFG110 no Configurador

2. Vamos tomar como exemplo uma numeração automática no campo A1\_COD da tabela de Clientes (SA1). Na imagem abaixo, note que existem 4 clientes cadastrados, portanto a última numeração é 000004:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025986251/2019-04-10_1001.png)

3. Na rotina APCFG110, a numeração deverá estar conforme a imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025986271/2019-04-10_1002.png)

Na área Números em uso / Números liberados, irá aparecer o que deverá ser o próximo número quando alguém incluir um novo Cliente, neste caso, 000005.

Na área Próximos números será exibido o número subsequente na ordem, neste caso, 000006.

Se por algum motivo, ao incluir um Novo Cliente na rotina de Clientes, a próxima numeração não estiver sendo 000005, então você deve clicar 2 vezes no número que está em Números em uso, alterar para o que seria o próximo, e na área Próximos números inserir o subsequente correto. Com isso você redefine a ordem que o sistema de numeração automática deve seguir.

O processo acima deverá ser executado para a tabela C20.

Passo 2:

Reiniciar os 3 serviços abaixo (muito importante)

a) Reiniciar o serviço do License Server

b) Reiniciar o serviço do DBAcces

c) Reiniciar o serviço do TAF (aplicação)
