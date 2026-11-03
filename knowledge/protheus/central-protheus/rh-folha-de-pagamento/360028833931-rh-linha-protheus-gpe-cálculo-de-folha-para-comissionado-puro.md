---
article_id: 360028833931
category: RH - Folha de Pagamento
content_hash: 72caa90c23f612260ed54a379beb78d390a62c08de892e003273443660fac77d
fetched_at: '2026-06-28T22:44:12.059382+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de Folha para comissionado puro
type: support-article
updated_at: '2025-09-15T19:36:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028833931-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Folha-para-comissionado-puro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17471433182487) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como realizar **cálculo de comissionado puro?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para executar o cálculo do comissionado puro, execute o procedimento conforme abaixo:  
  
Acesse Atualizações -> Funcionários -> Funcionário. Preencha o campo **Cat. Func com C e deixe o campo salário com 0,00.** As informações contidas nesta rotina serão armazenados na tabela **SRA**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101345593)

2. Acesse Atualizações -> Cadastros -> Verbas e crie uma verba atrelada ao identificador de cálculo **0165 - Pagamento Comissão e 0166 - DSR Comissão** conforme imagem abaixo. As informações contidas nesta rotina serão armazenados na tabela **SRV;**  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101345653)  
  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099114454)  
  
3. Acesse Atualizações -> Lançamentos -> Por Funcionário (GPEA580), e informe no roteiro FOL o valor de comissão através da verba criada com ID 0165;  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000234782)  
  
![](http://tdn.totvs.com/download/attachments/243637366/image2016-7-8%2011%3A15%3A59.png?version=1&modificationDate=1467987990000&api=v2)  
  
4. Execute o cálculo da folha em Miscelânea -> Cálculos -> Por Roteiro - GPEM020;  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099114754)  
  
5. Em Consultas -> Cálculos -> Por funcionário (GPEA090), consulte o cálculo gerado;  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099115094)  
  
OBS: Para que consiga realizar este processo, os campos de **Salário** - **RA\_SALÁRIO** e/ou **Salário Base Dissídio - RA\_ANTEAUM, não podem ser definidos como obrigatório no configurador. Por padrão do sistema, já por conta de cálculos que não usam salário fixo, os campos não são obrigatórios.**  
Neste caso, se na sua base os campos estiverem obrigatórios e não conseguir salvar com conteúdo 0,0, deve ajustar os mesmos no configurador, retirando a obrigatoriedade. Para isso, acesse o **Configurador - Base de Dados - Dicionário - Arquivos**, localize a tabela **SRA**, busque pelo campo **RA\_SALARIO**, edite o mesmo, **na aba Uso**, **desmarque a caixa "Obrigatório"**e **salve**. Após isso, **faça o mesmo processo para o campo RA\_ANTEUM caso ele também esteja como obrigatório.**  
  
Após isso, clique no ícone do **Disquete para atualizar a base de dados** e então, no próximo acesso ao SIGAGPE conseguirá cadastrar com o salário em branco.   
 

**Saber mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como realizar admissão de comissionado puro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4420684082071-RH-Linha-Protheus-GPE-Como-realizar-admiss%C3%A3o-de-comissionado-puro?source=search)

[RH - Linha Protheus - GPE - Como calcular 1° Parcela de 13° Salário para categoria comissionado puro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412810893591-RH-Linha-Protheus-GPE-Como-calcular-1-Parcela-de-13-Sal%C3%A1rio-para-categoria-comissionado-puro?source=search)

[RH - Linha Protheus - GPE - Como configurar o Sistema para calcular médias no afastamento para funcionários comissionados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058704233-RH-Linha-Protheus-GPE-Como-configurar-o-Sistema-para-calcular-m%C3%A9dias-no-afastamento-para-funcion%C3%A1rios-comissionados?source=search)

[RH - Linha Protheus - GPE - Cálculo da folha para Comissionado Puro quando possui afastamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019194451-RH-Linha-Protheus-GPE-C%C3%A1lculo-da-folha-para-Comissionado-Puro-quando-possui-afastamento-?source=search)

[RH - Linha Protheus - GPE - Como considerar outras verbas além de comissão para o cálculo de médias na ausência de funcionário comissionado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8248914155159-RH-Linha-Protheus-GPE-Como-considerar-outras-verbas-al%C3%A9m-de-comiss%C3%A3o-para-o-c%C3%A1lculo-de-m%C3%A9dias-na-aus%C3%AAncia-de-funcion%C3%A1rio-comissionado?source=search)

[RH - Linha Protheus - GPE - Como parametrizar o cálculo de Horas Extras/RSR para Comissionado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012420731-RH-Linha-Protheus-GPE-Como-parametrizar-o-c%C3%A1lculo-de-Horas-Extras-RSR-para-Comissionado?source=search)

[RH - Linha Protheus - GPE - Desconto de faltas e atrasos para comissionado puro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041228333-RH-Linha-Protheus-GPE-Desconto-de-faltas-e-atrasos-para-comissionado-puro?source=search)
