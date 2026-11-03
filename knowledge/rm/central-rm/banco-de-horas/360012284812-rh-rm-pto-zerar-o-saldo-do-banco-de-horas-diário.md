---
article_id: 360012284812
category: Banco de Horas
content_hash: fdabbad65c0464f0a6f065448f69cb6148f45ae680199d9c366fbf98def57c09
fetched_at: '2026-06-28T22:46:27.825953+00:00'
product: rm
section_id: 1500000835081
source: central-rm
title: RH - RM - PTO - Zerar o saldo do banco de horas diário
type: support-article
updated_at: '2025-01-31T11:08:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012284812-RH-RM-PTO-Zerar-o-saldo-do-banco-de-horas-di%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16039820987287) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**Como zerar o saldo do banco de horas diário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**Para zerar o banco de horas diário, siga os passos dos vídeos abaixo:  
  
​- Parte 1: Conferência de saldo e do tipo de banco de horas:  
  
  
- Parte 2: Parametrização e processo de compensação e lançamento do banco de horas:

**Importante**: Gostaríamos de ressaltar a importância de não selecionar o parâmetro '**Considere as horas originais que foram compensadas/pagas no banco de horas**' durante o processo. Ao marcá-lo, o sistema irá considerar todo o saldo do banco de horas, incluindo as horas que já foram compensadas ou lançadas em outros períodos. Em caso de necessidade de recálculo do ponto para desfazer a compensação ou lançamento no banco de horas, todo o saldo acumulado desde o início da utilização do banco será desfeito, não apenas o intervalo de datas especificado na rotina.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21455320855703)

E abaixo segue a descrição dos passos:

1. Acesse o módulo de **Automação de Ponto**, selecione a guia **Banco de horas** e clique no menu **Compensação/Lançamento do Banco de Horas**.  
   ![2019-02-19_17_17_26-TOTVS_S_rie_T_Servi_os__RM__Alias__CorporeRM___1-TOTVS_SA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360021848851)
2. Na primeira tela de parametrização, é necessário selecionar o tipo de banco como **Diário**, e o tipo da compensação como **Considera as horas que estão no banco de horas (Padrão)**. O período a ser compensado/lançado deverá abranger todo o banco de horas do funcionário (início de utilização até último dia do período a ser zerado). Em relação às opções do banco de horas, caso seja selecionada a opção  **Lançamento do banco de horas**, a tela de **Compensação do banco de horas** não será apresentada.  
   ![2019-02-19_17_00_36-Compensa__o_e_ou_Lan_amento_do_Banco_de_Horas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360021879772)  

   **Importante**: Gostaríamos de ressaltar a importância de não selecionar o parâmetro '**Considere as horas originais que foram compensadas/pagas no banco de horas**' durante o processo. Ao marcá-lo, o sistema irá considerar todo o saldo do banco de horas, incluindo as horas que já foram compensadas ou lançadas em outros períodos. Em caso de necessidade de recálculo do ponto para desfazer a compensação ou lançamento no banco de horas, todo o saldo acumulado desde o início da utilização do banco será desfeito, não apenas o intervalo de datas especificado na rotina.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21455320855703)
3. Na tela de **Compensação do banco de horas**, as **Opções de Compensação** devem ser marcadas\desmarcadas de acordo com a regra de negócio do banco de horas do cliente. Para maiores informações sobre o que cada opção realiza, consulte a seção **Saiba Mais** deste artigo. As ordenações deverão permanecer conforme print.  
   ![2019-02-19_17_05_14-Compensa__o_e_ou_Lan_amento_do_Banco_de_Horas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360021848751)
4. Na primeira tela de **Lançamento do banco de horas para o movimento**, as opções para lançamento deverão estar **desmarcadas** e as ordenações deverão permanecer conforme print.  
   ![2019-02-19_17_06_43-Compensa__o_e_ou_Lan_amento_do_Banco_de_Horas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360021848771)
5. Na segunda tela de **Lançamento do banco de horas para o movimento**, a parametrização poderá ser realizada conforme print.  
   ![2019-02-19_17_07_22-Compensa__o_e_ou_Lan_amento_do_Banco_de_Horas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360021848891)

**Saiba Mais**  
Para maiores informações sobre o processo de **Compensação\Lançamento do Banco de horas**, acesse a documentação [Compensação\Lançamento do Banco de Horas - Parâmetros.](https://tdn.totvs.com/pages/releaseview.action?pageId=452719612)
