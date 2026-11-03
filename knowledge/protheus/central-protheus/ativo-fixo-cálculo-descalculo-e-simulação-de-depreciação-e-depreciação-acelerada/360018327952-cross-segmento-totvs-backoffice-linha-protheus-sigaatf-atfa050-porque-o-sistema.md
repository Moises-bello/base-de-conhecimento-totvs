---
article_id: 360018327952
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 9873a801d321e722e0a44ff8db51c086afb07c94487548f8c8dd87d510b055b9
fetched_at: '2026-06-28T22:41:43.330428+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAATF - ATFA050 - Porque
  o sistema não calcularia a depreciação de um bem?
type: support-article
updated_at: '2026-05-04T17:32:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018327952-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Porque-o-sistema-n%C3%A3o-calcularia-a-deprecia%C3%A7%C3%A3o-de-um-bem
---

O sistema não calcula a depreciação de um bem se faltar cadastro de contas contábeis, taxa de depreciação, ou se o bem estiver totalmente depreciado. A depreciação termina quando a soma da depreciação acumulada e correção iguala o valor original corrigido. O cálculo deve usar data base no último dia do mês, posterior ao parâmetro MV\_ULTDEPR. Mensagens comuns indicam problemas como falta de moedas, datas fora do parâmetro e saltos de período.

**Dúvida**  
Por que o sistema não calcularia a depreciação de um bem?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - Todas as versões  
  
  
**Solução**  
Para que o cálculo de depreciação seja processado corretamente, o sistema deverá validar algumas condições:

1. Caso o bem não possua contas contábeis cadastradas, não tenha taxa de depreciação informada ou o valor da depreciação acumulada seja igual ao valor original, entende-se que o bem já foi totalmente depreciado, o que impede o cálculo da depreciação.
2. Se o bem estiver sujeito à correção monetária, o término da depreciação ocorrerá quando:  
     
   **Depreciação acumulada + Correção da depreciação acumulada = Valor original + Correção do bem**.
3. O cálculo de depreciação deve ser sempre realizado com a data base no último dia do mês e, obrigatoriamente, posterior à data definida no parâmetro MV\_ULTDEPR.

[ATFA050 - Não processa o calculo de depreciação mensal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018327952-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-Porque-o-sistema-n%C3%A3o-calcularia-a-deprecia%C3%A7%C3%A3o-de-um-bem)

**Mensagens de HELP comuns**:

1. **AF050MOEDA**: Indica que faltam cadastros de moedas para todos os dias do mês.  
     
   Seguir documentação abaixo para correção do erro:  
   [Moedas não cadastradas - AF050MOEDA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009398152-Cross-Segmento-Backoffice-Linha-Protheus-MOEDAS-N%C3%83O-CADASTRADAS-AF050MOEDA)
2. **050JACALC**: Essa mensagem ocorre quando a data base informada ao entrar no sistemaé anterior ao valor do parâmetro **MV\_ULTDEPR**, ou seja, o cálculo já foi processado anteriormente.   
     
   Por exemplo:  
   Data-base em 28/02/2026:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40217900465431)

   Parâmetro MV\_ULTDEPR em 31/03/2026:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40217900466455)
3. **050DTDEPR**: indica que há um salto de período no cálculo. Exemplo: se MV\_ULTDEPR = 29/02/2026 e a data base informada for 30/04/2026, o sistema sinaliza que o mês de março foi ignorado.  
     
   OBS.: O parâmetro **MV\_ULTDEPR** é criado separadamente por filial, ou seja, cada filial da empresa possui o seu parâmetro, sendo necessária a análise de qual filial está realizando o cálculo de depreciação.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40217884120855)

   Caso esteja realizando o cálculo de depreciação para apenas uma filial, e o erro persista, verifique o parâmetro **MV\_ATFCTRL,** se ele está ativado. Caso este parâmetro esteja ativado, ao realizar o Cálculo Mensal (ATFA050), sempre será executado em todas as filiais.  
     
   [MV\_ATFCTRL - Como configurar o controle de transações no cálculo de depreciação dos ativos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038362194-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-MV-ATFCTRL-Como-configurar-o-controle-de-transa%C3%A7%C3%B5es-no-c%C3%A1lculo-de-deprecia%C3%A7%C3%A3o-dos-ativos)

**Saiba mais:**  
[Utilização de procedure no cálculo de depreciação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021716291?source=search)  
[Erro na chamada de processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420151614743?source=search)
