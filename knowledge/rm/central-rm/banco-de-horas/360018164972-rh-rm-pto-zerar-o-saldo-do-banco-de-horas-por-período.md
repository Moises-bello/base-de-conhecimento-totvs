---
article_id: 360018164972
category: Banco de Horas
content_hash: b752c0addf1cede1a2125b0fb874eb632914bf0a4a84b8e8e4eb022e9967ec55
fetched_at: '2026-06-28T22:46:27.808477+00:00'
product: rm
section_id: 1500000835081
source: central-rm
title: RH - RM - PTO - Zerar o saldo do banco de horas por período
type: support-article
updated_at: '2024-12-05T16:41:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018164972-RH-RM-PTO-Zerar-o-saldo-do-banco-de-horas-por-per%C3%ADodo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16981762188183) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Como zerar o saldo do banco de horas por período?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 11.80  
  
**Solução**Para zerar o saldo do banco de horas por período, siga dos vídeos abaixo de como realizar o processo:  
  
Parte 1 - Conferência do saldo antes de realizar o processo:  
  
  
Parte 2 - Realização do processo:

Gostaríamos de ressaltar a importância de não selecionar o parâmetro '**Considere as horas originais que foram compensadas/pagas no banco de horas**' durante o processo. Ao marcá-lo, o sistema irá considerar todo o saldo do banco de horas, incluindo as horas que já foram compensadas ou lançadas em outros períodos. Em caso de necessidade de recálculo do ponto para desfazer a compensação ou lançamento no banco de horas, todo o saldo acumulado desde o início da utilização do banco será desfeito, não apenas o intervalo de datas especificado na rotina.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21455172328727)

Parte 3 - Conferência do saldo após execução do processo:

Caso deseje, abaixo segue a descrição do passo a passo:

1. Dentro do espelho do funcionário em **Janelas de Informações**, nas abas **Saldo de banco de horas sintético** e **Banco de horas**, verifique as horas presentes no banco de horas do funcionário e certifique-se de que o tipo de banco é **Período**.  
   ![2018-10-19_09_00_24-Espelho_do_Funcion_rio_00002_-_JOAO_DA_SILVA_JORDAM.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013753851)
2. Identifique o primeiro período do banco de horas do funcionário (último período que o funcionário estava com saldo zerado) através da aba **Saldo de banco de horas sintético**. Este passo é importante pois caso o primeiro período não seja selecionado para a compensação e lançamento, o saldo do período ativo não será zerado.  
   ![2018-10-19_08_58_23-Espelho_do_Funcion_rio_00002_-_JOAO_DA_SILVA_JORDAM.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013739472)
3. Acesse a aba **Banco de horas** e selecione o menu **Compensação/Lançamento do Banco de Horas**.  
   ![2018-10-19_09_24_56-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013739772)
4. Selecione a **Definição do banco de horas** como **Período**, informe o primeiro período do banco de horas do funcionário e selecione a opção **Compensação e lançamento do banco de horas** nas **Opções de banco de horas**.  
     
   ![2018-10-19_09_14_49-Compensa__o_e_ou_Lan_amento_do_Banco_de_Horas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013739492)  

   Gostaríamos de ressaltar a importância de não selecionar o parâmetro '**Considere as horas originais que foram compensadas/pagas no banco de horas**' durante o processo. Ao marcá-lo, o sistema irá considerar todo o saldo do banco de horas, incluindo as horas que já foram compensadas ou lançadas em outro períodos. Em caso de necessidade de recálculo do ponto para desfazer a compensação ou lançamento no banco de horas, todo o saldo acumulado desde o início da utilização do banco será desfeito, não apenas o intervalo de datas especificado na rotina.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21455172328727)
5. Na tela **Compensação de banco de horas** e na primeira tela de **Lançamento do banco de horas para o Movimento**, realize a parametrização conforme sua demanda. Segue exemplos abaixo.  
   ![2018-10-19_09_03_10-Compensa__o_e_ou_Lan_amento_do_Banco_de_Horas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013753891)  
     
   ![2018-10-19_09_03_13-Compensa__o_e_ou_Lan_amento_do_Banco_de_Horas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013753911)
6. Na segunda tela de **Lançamento do banco de horas para o Movimento**, selecione o **Tipo de lançamento** como **Período** e a **Forma de Lançamento** como **Somente acima do número de horas**. Marque as opções **Extras**, **Atrasos** e **Faltas** em **Considera total das horas** e zere os campos de cada opção.  
   ![2018-10-19_09_03_23-Compensa__o_e_ou_Lan_amento_do_Banco_de_Horas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013753931)
7. Execute o processo e ao finalizar acesse o espelho do funcionário para verificar os valores. A aba **Saldo de banco de horas sintético** deverá estar com o saldo zerado e aba **Movimento** deverá possuir os eventos lançados conforme cadastro no sindicato.  
   ![2018-10-19_09_07_12-Espelho_do_Funcion_rio_00002_-_JOAO_DA_SILVA_JORDAM.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013753951)  
     
   ![2018-10-19_09_08_05-Espelho_do_Funcion_rio_00002_-_JOAO_DA_SILVA_JORDAM.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013753971)

**Importante**

1. Com o processo acima, todas as horas do primeiro período selecionado até o período ativo, serão compensadas do banco de horas e as horas remanescentes serão enviadas para o movimento do funcionário.  
   ![2018-10-19_09_16_54-Espelho_do_Funcion_rio_00002_-_JOAO_DA_SILVA_JORDAM.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013753991)
2. Na aba **Saldo de banco de horas sintético**, apenas o saldo do período **ativo** será atualizado.

**Saiba mais**  
Para maiores informações sobre parametrizações do banco de horas por período, acesse o artigo   
[RH - RM - PTO - Como configurar o banco de horas por período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017559512)
