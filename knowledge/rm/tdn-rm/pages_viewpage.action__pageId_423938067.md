---
content_hash: 4a114dbe2180ae1a4c73b99f108f8b6b56e9a3b5ab355500859488c7b6261a66
fetched_at: '2026-06-29T00:09:25.219191+00:00'
page_id: '423938067'
product: rm
source: tdn-rm
title: Custeio da Produção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938067
version: 1
---

**Custeio da Produção**

---

**Custos Indiretos**   
São custos cujo vínculo com a produção de uma unidade do produto acabado não são identificados.  
As parametrizações do custo são de suma importância para o calculo do MRPII. Para parametrizar o custo acesse o menu Opções | Parâmetros | Produção pasta Custos. Existem três formas de parametrizar o Custo Indireto:  
1) Não Considerar O custo indireto será zero.  
2) Majoração do Valor de Mão de Obra Direta Será aplicado o Índice de Majoração de Mão de Obra sobre o valor total da mão de obra alocada na Ordem de Produção. Para cadastrar o Índice de Majoração de Mão de Obra acesse o menu Cadastros | Índices de Majoração por Mão de Obra. O custo indireto será o custo da mão de obra vezes o percentual do índice de majoração. Se o cadastro de Índice de Majoração de Mão de Obra não possuir índice referente ao mês atual o sistema irá aplicar o último índice dentro dos últimos 12 meses. Caso o índice seja anterior a 12 meses, o sistema não considera o índice e retorna o custo indireto igual a zero.  
**Exemplo:** Uma alocação de mão de obra em uma atividade com data de início 22/09/2009 08:00:00 e data final 22/09/2009 09:10:00 = 10 minutos para executar a atividades onde foi alocado. Se o custo da mão de obra é R$ 5,00 reais hora. Logo o custo de 10 minutos será R$ 0,83 centavos. 0,83 \* 10 %(índice de majoração)=0,08.  
Após calcular o custo de majoração de todas as mãos de obras alocadas o sistema soma todos os índices de majoração calculados exibindo o custo indireto da ordem de produção.  
3) Custo Unitário Indireto Será o valor do custo hora cadastrado na estrutura vezes a quantidade de produto acabado a ser fabricado    
**Custos Diretos**  
São custos que estão vinculados diretamente à produção de uma unidade do produto acabado. Exemplo: matéria prima e mão de obra.  
Observações: Para o conceito de mão de obra direta multifuncional (o mesmo operador cuida pessoalmente de várias ordens de produção ao mesmo tempo) teremos o método de rateio por custo indireto.  
**Custo do Componente**  
Para parametrizar o custo do componente acesse o menu Opções | Parâmetros | Produção, pasta Movimentação de Estoque campo "Origem do Custo da Matéria Prima", que poderá ser "Custo Médio", "Custo Unitário", "Custo Reposição A" ou "Custo Reposição B".

* Verificar o valor do custo do produto no TOTVS Gestão de Estoques, Compras e Faturamento no anexo "Saldos e Custos" de acordo com o custo parametrizado;
* O cálculo será:  
  a quantidade de componte usado para produzir o acabado ou semiacado vezes  a quantidade do acabado ou semicado que será produzido vezes o valor do custo no RM Nucleus.    
  QCP\*QP\*CN = Custo do componente  
     
  **Custo da Mão de Obra**  
  O custo de mão de obra será cadastrado no menu Cadastros | Mão de Obra, na pasta Custo. O custo pode ser informado manualmente ou através de planilha da Linha RM que possibilita contemplar a integração com TOTVS Folha de Pagamento.  
  **Exemplo:** Data final prevista menos data inicial prevista da alocação da mão-de-obra na atividade 15:49:48 – 15:39:52 = 00:10:04 10 minutos \* 60 = 600 para transformar em segundos, logo 600 + 4 segundos Se o custo da mão de obra é R$ 5,00 à hora 5/360 para achar o custo em segundos = 0,001388 Logo o custo da mão-de-obra será o custo em segundos \* a duração em segundos (0,0013888\*604=0,8389).  
  **Observações:** O sistema irá alocar inicialmente as mãos de obra de menor custo.    
  **Custo do Posto de Trabalho**  
  O custo do posto de trabalho será cadastrado no menu Cadastros | Postos de Trabalho, na pasta Custo. O custo pode ser informado manualmente ou através da planilha da Linha RM.  
  Data final prevista menos data inicial prevista da atividade 09:24:18 – 09:19:18 = 00:05:00 5 minutos \* 60 = 300 para transformar em segundos, logo 300 segundos Se o custo do posto é R$ 20,00 à hora. 20/360 para achar o custo em segundos = 0,06 Logo o custo do posto será o custo em segundos \* a duração em segundos (0,06\*300=16,67). CPT = DATV \* CHP    
  **Custo do Equipamento**  
  O custo do equipamento será cadastrado no menu Cadastros | Equipamentos, na pasta Custo. O custo pode ser informando manualmente ou através da planilha da Linha RM.  
  Data final prevista menos data inicial prevista da alocação do equipamento na atividade 08:12:19 – 08:02:19 = 00:10:00 10 minutos \* 60 = 600 para transformar em segundos, logo 600 segundos. Se o custo do equipamento é R$ 2,00 à hora. 2/360 para achar o custo em segundos = 0,01. Logo o custo do equipamento será o custo em segundos \* a duração em segundos (0,01 \* 600 = 3,33).    
  **Custo de Subproduto Gerado**  
  O custo de subproduto será obtido através da parametrização. Para parametrizar o custo acesse o menu Opções | Parâmetros | Produção, pasta Custos. Existem quatro opções de parametrização:  
  1) Não Definir Custos O sistema irá retornar zero no custo do subproduto gerado.  
  2) Utilizar Custo do RM Nucleus O valor do custo do subproduto no TOTVS Gestão de Estoques, Compras e Faturamento é verificado no anexo "Saldos e Custos" no local de estoque para subproduto. CSP= QSG \* CN   
  3) Utilizar Percentual Sobre o Processo Produtivo Quando o custo do subproduto for sobre o proceso produtivo, o custo unitário do subproduto será o custo da atividade vezes o percentual cadastrado no debita custo, dividido pela quantidade de subproduto gerado na atividade. CUSP = CATV \* PSP / QSG  
  4) Utilizar Custo por Fórmula O custo unitário do subproduto será o valor retornado pela fórmula dividido pela quantidade de subproduto gerado.  
  **Exemplo:** SELECT NVL ((SUM(CUSTOEFETIVADO)+SUM(CUSTO))\* 0.10,10) AS CUSTOSUBPRODUTO FROM KATVORDEM WHERE CODCOLIGADA = 1 AND   CODFILIAL = 1 AND   CODORDEM = 'OP-0022/09' AND   CODESTRUTURAFEITA = 'IOEST001' AND   IDATVORDEM >= 1;    
  **Custo do Semiacabado**  
  O custo do semiacabado será composto pelo custo dos componentes para fabricá-lo, custo do posto, custo da mão de obra, custo do equipamento, custo subproduto (quando alguma atividade da estrutura do semiacabado gerar subproduto) e custo indireto. Lembrando que o custo indireto é sobre o acabado.    
  **Custo da Atividade**  
  O custo da atividade é composto pelo custo da mão de obra, custo do posto, custo do equipamento e custo do componente. CATV = CMO + CPT + CEQ + CMP    
  **Custo do Item da Ordem**  
  A composição do custo do item da ordem de produção é o somatório do custo das atividades  custo indireto  o percentual do debita custo do subproduto gerado. CITEM = Σ CATV + CI – PSP    
  **Legenda:**  
  Sigla - Descrição  
  DATV  Duração da Atividade QCP - Quantidade do Componente QP  Quantidade a Produzir QSG - Quantidade de Subproduto Gerado na Atividade PSP - Percentual do Subproduto Cadastrado no Debita Custo CMP - Custo do Componente (Materia Prima e/ou Semiacabado) CMO - Custo da Mão de Obra CPT - Custo do Posto de Trabalho CHP - Custo Hora do Posto de Trabalho CD - Custo Direto CI - Custo Indireto CSA - Custo do Semiacabado CEQ - Custo do Equipamento CHEQ - Custo Hora do Equipamento CSP - Custo do Subproduto CUSP - Custo Unitário de Subproduto CATV - Custo da Atividade CITEM - Custo do Item da Ordem CN - Custo do TOTVS Gestão de Estoques, Compras e Faturamento "Custo Médio", "Custo Unitário", "Custo Reposição A" ou "Custo Reposição B" Σ - Somatório
