---
article_id: 18000554140695
category: GPE - eSocial - Processo Trabalhista
content_hash: b7748a3eec6e330641b93cb9a76068c7922a07dad6d60e5f7cede95ed9387148
fetched_at: '2026-06-28T22:45:00.609157+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2501 - Como preencher o grupo Identificação
  do período e da base de cálculo dos tributos
type: support-article
updated_at: '2024-11-04T12:34:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18000554140695-RH-Linha-Protheus-GPE-eSocial-S-2501-Como-preencher-o-grupo-Identifica%C3%A7%C3%A3o-do-per%C3%ADodo-e-da-base-de-c%C3%A1lculo-dos-tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18000524746775) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como preencher o grupo Identificação do período e da base de cálculo dos tributos, de acordo com o leiaute S-1.2 para o evento S-2501?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O preenchimento dos campos da rotina **Dados eSocial,** para inclusão de periodo e base de calculo dos tributos, deve ser seguido o leiaute vigente.  
[Veja o caminho e como incluir um Tributo (S-2501).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12072324087575)  
Acesse a aba **Informação do período e base de cálculo**  (*Tag* gerada no S-2501 [calcTrib](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/index.html#r_2501_ideTrab_calcTrib)) e clique em **+ Incluir Periodo**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27538244226839)  
  
Clique em **Informação de Periodo** para inclusão da Referencia, valor de base de calculo e valor da base de calculo de 13º.  
Após preencher as informações, clique em Salvar Periodo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27538216655767)  
  
**1- Referencia** - *Tag* **perRef**: Informar o mês/ano (formato AAAA-MM) de referência das informações.  
Deve ser um **período existente no evento S-2500** para o trabalhador indicado em cpfTrab e igual ou posterior a [2008-12]. De acordo com o campo **Competência inicial** informado no S-2500.  
  
**2- Valor da base de cálculo da contribuição previdenciária sobre a remuneração mensal do trabalhador** - *Tag* **vrBcCpMensal:** Deve ser maior ou igual a 0 (zero).  
  
**3- Valor da base de cálculo da contribuição previdenciária sobre a remuneração do trabalhador referente ao 13º salário** - *Tag* **vrBcCp13:** Deve ser maior ou igual a 0 (zero).  
  
Após preencher os campos conforme leiaute vigente S-1.2, clique em **Contribuições Sociais cadastradas para este periodo,** para informar o **grupo infoCRContrib** Informações das contribuições sociais devidas à Previdência Social e Outras Entidades e Fundos, por Código de Receita - CR:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27538216657687)  
  
**Código de Receita** - Tag **tpCR**: CR relativo a contribuições sociais devidas à Previdência Social e a Outras Entidades e Fundos (Terceiros), conforme legislação em vigor na competência.  
Validação**:** Deve ser um código válido e existente na [Tabela 29](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/tabelas.html#29).  
  
**Valor** correspondente ao Código de Receita - CR - Tag **vrCR**:  
Validação**:** Deve ser informado de acordo com a legislação em vigor na competência.  
Deve ser maior que 0 (zero).  
  
Clique em **+ Salvar Contribuição** após finalizar o cadastro das informações conforme leiaute vigente S-1.2.  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".*
