---
article_id: 8191950951447
category: RH - 13º salário
content_hash: 7d607128f291a160543c46b9ea0125705fc92e78789bca173b41b9c8fd0d1600
fetched_at: '2026-06-28T22:44:00.626234+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar o cálculo da 1° parcela do 13º salário
type: support-article
updated_at: '2025-08-06T11:25:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8191950951447-RH-Linha-Protheus-GPE-Como-efetuar-o-c%C3%A1lculo-da-1-parcela-do-13%C2%BA-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17959395044631) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como efetuar o cálculo da primeira parcela do 13º salário para apenas um funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Acesse rotina de **Períodos** através do menu **Atualizações >Definições de Cálculo >Períodos**;  
  
2. Cadastre no **período em aberto** o Roteiro **131** (para cálculo da primeira parcela do 13º):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8206198662551)

3. Acesse a **rotina de Cálculo por Roteiro** através do menu **Miscelânea >Cálculos >Por Roteiros** e selecione processo para cálculo e o roteiro 131 (neste exemplo utilizamos processo 00001 - CELETISTA/ESTAGIÁRIO MENSAL):

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9799720782743)

4. Confirme período e número de pagamento preenchidos pelo sistema e clique em **OK**;  
  
5. Automaticamente o sistema abrirá a tela de parâmetros, para que seja possível personalizar o cálculo de acordo com as necessidades da empresa. Preencha os parâmetros conforme desejado e clique em **OK**;  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9799790454167)  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9799792885399)

**Exemplo:**

* Ordem: Matricula;
* Percentual: 50% (Metade do salário);
* Calcula médias: SIM ou NÃO;
* Arredondamento: SIM ou NÃO;
* Complementa 1ª parcela: Selecione esta opção caso tenha funcionário que já tenha recebido a primeira parcela do ano corrente em outra ocasião e tiveram aumento de salário; Esta informação calcula esta diferença. Se informar conteúdo = NÃO, o sistema pagará as diferenças apenas na segunda parcela;
* Data de Referência: Define qual a base deseja utilizar para o cálculo. Informando 30/11 o sistema utilizará 11 avos e pagará 50%, ou seja 5,5 avos ao invés de 6. Por isso sempre orientamos a deixar com o ultimo dia do ano 31/12;
* Referência média?: Define se deseja considerar a data atual, ou seja, o mês do cálculo para média;
* Considera mês atual: Informe se deseja que o Mês/Ano de referência seja considerado para cálculo da média por sindicato.

6. Para filtrar um funcionário, acesse um dos dois tipos de filtro:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9799797948183)  
  
Como exemplo, usei o “**Alterar Filtro**”  
  
7. No campo matrícula coloque o número da matrícula do funcionário que deseja calcular, informe a categoria do funcionário e clique em **Confirmar**:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9799815038359)  
  
8. Após selecionar todos os parâmetros e filtrar o funcionário, clique em **Calcular**:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9799820179095)  
  
9. Log de cálculo:  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9800138187287)  
  
10. Para visualização do cálculo acesse o menu **Atualizações > Lançamentos >Lançamentos Por funcionário**, selecione a matrícula que deseja conferir o cálculo e clique em **Visualizar**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17959442339991)  
  
11. Altere o Roteiro para **131;  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9800115729175)**12. Pode-se calcular o roteiro 131 pela rotina de **Lançamento por funcionário** através do menu **Atualizações >Lançamentos >Por Funcionário;  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9800142281623)**

13. Selecione o funcionário e clique em **Incluir** ou **Alterar** (opção Alterar se o funcionário já possui lançamentos):  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9800211974679)  
  
14. Informe o Roteiro **131** e em **Outras Ações** selecione **Calcular Lançamento (F6)**;  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9800237263895)  
  
15. Preencha os parâmetros e clique em **OK** (observe o passo 5);

16. Após o processamento, consulte o cálculo em **Outras Ações** selecionando a opção de **Consultar Cálculo(F7)** ou **Recibo de Pgto:  
  
![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9800439040919)**17. Exemplo da opção **Consultar Cálculo.**

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9800445794455)

**Observações:** Na versão 12, o cálculo da primeira parcela não é apresentado no roteiro FOL, sendo apenas considerada dentro da competência onde foi calculada no roteiro 131-Primeira Parcela.

Após cálculo e conferência é necessário fechar o Roteiro 131 para que este seja gravado no acumulado (NÃO HÁ NECESSIDADE DE INTEGRAÇÃO).

**Saber Mais:**

[RH - Linha Protheus - GPE - Como parametrizar o sistema para que a 1ª Parcela do 13º Salário considere até a competência atual ou até dezembro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016125111-RH-Linha-Protheus-GPE-Como-parametrizar-o-sistema-para-que-a-1%C2%AA-Parcela-do-13%C2%BA-Sal%C3%A1rio-considere-at%C3%A9-a-compet%C3%AAncia-atual-ou-at%C3%A9-dezembro?source=search)

[RH - Linha Protheus - GPE - Como não calcular 1ª parcela do 13º para funcionários em período de experiência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6676087304855-RH-Linha-Protheus-GPE-Como-n%C3%A3o-calcular-1%C2%AA-parcela-do-13%C2%BA-para-funcion%C3%A1rios-em-per%C3%ADodo-de-experi%C3%AAncia?source=search)  
[RH - Linha Protheus - GPE - Como gerar memória de calculo para conferência de médias da primeira parcela do 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000096841-RH-Linha-Protheus-GPE-Como-gerar-mem%C3%B3ria-de-calculo-para-confer%C3%AAncia-de-m%C3%A9dias-da-primeira-parcela-do-13%C2%BA?source=search)  
[RH - Linha Protheus - GPE - Relatório de Memória de Cálculo no 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058080854-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Mem%C3%B3ria-de-C%C3%A1lculo-no-13%C2%BA?source=search)

[RH - Linha Protheus - GPE - Sistema não calcula verbas de médias no 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016249711-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-verbas-de-m%C3%A9dias-no-13%C2%BA-sal%C3%A1rio?source=search)  
[RH - Linha Protheus - GPE - Como cancelar o cálculo de 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059539553-RH-Linha-Protheus-GPE-Como-cancelar-o-c%C3%A1lculo-de-13%C2%BA-Sal%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Sistema não calcula para alguns funcionários 1 parcela do 13 salario, Pela EndCalc() - S\_ADT13PGT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039131954-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-para-alguns-funcion%C3%A1rios-1-parcela-do-13-salario-Pela-EndCalc-S-ADT13PGT?source=search)

[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
