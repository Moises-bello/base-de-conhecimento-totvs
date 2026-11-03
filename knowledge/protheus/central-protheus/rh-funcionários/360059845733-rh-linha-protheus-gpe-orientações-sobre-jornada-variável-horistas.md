---
article_id: 360059845733
category: RH - Funcionários
content_hash: ade29687901bf41476411203199996237adf810bd9981c7ccc66fe288dbeda52
fetched_at: '2026-06-28T22:43:28.638269+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Orientações sobre Jornada Variável Horistas
type: support-article
updated_at: '2025-08-06T17:41:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059845733-RH-Linha-Protheus-GPE-Orienta%C3%A7%C3%B5es-sobre-Jornada-Vari%C3%A1vel-Horistas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26438789779223) Tempo aproximado para leitura: 00:01:00 min****Dúvida**Qual funcionalidade do campo Jornada Variável (RA\_HOJORVA)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17

**Solução:**O funcionário horista com Jornada Variável é aquele cuja quantidade de horas trabalhadas no mês **sofre variações** de acordo com a necessidade de suas atribuições.  
Já o funcionário com jornada homogênea é o empregado cuja jornada é **fixa e não oscila.**  
  
Desta forma, o salário referência utilizado para o pagamento de Férias, 13º salário e Aviso Prévio, de funcionários com jornada variável, deverá ser obtido através da **média das horas apuradas dos 12 últimos meses.**  
  
Para atender a esta demanda foi implementada no sistema, a opção para o cálculo de salário referência a ser utilizado nas Férias, 13º Salário e Aviso Prévio, a partir da média de Horas.

**Cadastro de Funcionários:**  
Incluído o campo Horista Jornada Variável (RA\_HOJORVA), que deve ser preenchido:

1-Sim (funcionário tem horas variáveis)  
2-Não  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33992910443287)

**Composição do Salário:**

**->** Serão consideradas como verbas de salário, ou seja, aquelas que serão consideradas na composição das médias salariais, todas as verbas que estiverem **agrupadas com** **0**, no Cadastro de Verbas (GPEA040), pasta Outras Informações, campo Grupo Verba (RV\_GRPVERB).

**->** Caso o funcionário seja Horista (RA\_CATFUNC = "H") e o novo campo Jor.Variavel (RA\_HOJORVA) tenha o conteúdo **1-Sim**, mas no cadastro de verbas nenhuma verba esteja no GRUPO 0 (RV\_GRPVER = "0"), a**média salarial não será calculada.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33992898663063)**

**Saiba Mais**[Horistas com Jornada Variável](https://tdn.totvs.com/display/public/PROT/TVMEN0_DT_Horistas_com_Jornada_Variavel)  
[RH - Linha Protheus - GPE - Como conferir o cálculo de funcionário horista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015195412-RH-Linha-Protheus-GPE-Como-conferir-o-c%C3%A1lculo-de-funcion%C3%A1rio-horista)  
[RH - Linha Protheus - GPE - Como cadastrar um Funcionário de categoria Horista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410258909335-RH-Linha-Protheus-GPE-Como-cadastrar-um-Funcion%C3%A1rio-de-categoria-Horista?source=search)
