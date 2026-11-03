---
article_id: 360024437412
category: Financeiro
content_hash: 64136b921763567ef005b74b4253a3b76ccdd98163d2e38910b8f919cd14c55f
fetched_at: '2026-06-28T22:38:03.275065+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Incluir um campo da
  mesma tabela no browser da rotina
type: support-article
updated_at: '2022-06-15T00:10:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024437412-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Incluir-um-campo-da-mesma-tabela-no-browser-da-rotina
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como incluir um campo da mesma tabela no browser da rotina?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Primeiramente verifique o nome do campo, altere ou incluía um registro na rotina, então clique sobre o campo e pressione **F1**  
  
![](http://tdn.totvs.com/download/attachments/271667775/CBR_01.png?version=1&modificationDate=1487269903000&api=v2)

**Importante**: O nome da tabela é formado pela letra **S** mais os 2 primeiros caracteres do nome do campo*.* No exemplo *(**A1\_BAIRRO**),* a tabela é **SA1***.*

Siga os passos abaixo:

1. Acesse **Configurador** > **Base de Dados** > **Dicionário** > **Bases de Dados**  
2. Clique em **Dicionário de Dados**, e pesquise pela tabela  
3. Clique sobre a tabela e clique em **Editar**  
  
![](http://tdn.totvs.com/download/attachments/271667775/CBR_02.png?version=1&modificationDate=1487269903000&api=v2)

4. Expandir a tabela, clique em **Campos**, e localize o campo que deseja alterar  
5. Clique sobre o campo, e clique em **Editar**  
  
![](http://tdn.totvs.com/download/attachments/271667775/CBR_03.png?version=1&modificationDate=1487269903000&api=v2)

6. Clique na aba **Uso**, marque a caixinha **Browse**  
  
![](http://tdn.totvs.com/download/attachments/271667775/CBR_04.png?version=1&modificationDate=1487269903000&api=v2)

7. Clique em **Salvar** (**Confirmar**), depois em **Confirmar**  
  
![](http://tdn.totvs.com/download/attachments/271667775/CBR_05.png?version=1&modificationDate=1487269903000&api=v2)

8. Na tela da listagem de tabelas, clique em **Atualizar base de dados**  
  
![](http://tdn.totvs.com/download/attachments/271667775/CBR_06.png?version=1&modificationDate=1487269903000&api=v2)

9.   Na tela **Atualização do Dicionário de Dados**, clique em **Avançar**  
10. Aguarde o processamento. Ao final, será exibida uma tela com a mensagem **Atualização finalizada com sucesso**. Clique em **Finalizar**.  
  
![](http://tdn.totvs.com/download/attachments/271667775/CBR_07.png?version=1&modificationDate=1487269903000&api=v2)  
  
Na rotina o campo será exibido no **Browse**:  
  
![](http://tdn.totvs.com/download/attachments/271667775/CBR_08.png?version=1&modificationDate=1487269903000&api=v2)

**Importante:**Este procedimento de **Atualizar base de dados** tem como finalidade confirmar a **inclusão do campo na tabela no banco de dados**. Deve ser feito em modo exclusivo, ou seja, não pode haver nenhum usuário com alguma rotina aberta que utilize a tabela envolvida.
