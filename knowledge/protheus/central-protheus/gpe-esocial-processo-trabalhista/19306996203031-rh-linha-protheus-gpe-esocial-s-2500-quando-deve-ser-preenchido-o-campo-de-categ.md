---
article_id: 19306996203031
category: GPE - eSocial - Processo Trabalhista
content_hash: 7f5752f0b22988f7f884589ad7f794cda44c2779c88e01fd67cc6c2d1050efcf
fetched_at: '2026-06-28T22:45:00.556662+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2500 - Quando deve ser preenchido o
  campo de categoria no S-2500
type: support-article
updated_at: '2024-11-01T19:50:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19306996203031-RH-Linha-Protheus-GPE-eSocial-S-2500-Quando-deve-ser-preenchido-o-campo-de-categoria-no-S-2500
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19306996194711) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quando deve ser preenchido o campo de categoria (codCateg) no grupo Informações do Contrato de Trabalho do evento S-2500?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No evento S-2500 existem campos que são inicialmente opcionais, mas que se tornam obrigatório dependendo do preenchimento de outro campo, como por exemplo o campo **Código da Categoria**, localizado na rotina **Dados eSocial**, no grupo **Informações do Contrato de Trabalho**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27498634125079)  
  
No leiaute do esocial S-1.2 existe a seguinte regra:  
**Validação:** Informação obrigatória e exclusiva se **[indContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/#2500_ideTrab_infoContr_indContr)****= [N]** **ou se o campo****[matricula](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/#2500_ideTrab_infoContr_matricula)****não estiver preenchido.**   
Deve ser um código válido e existente na [Tabela 01](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/tabelas.html#01) e obedecer ao que segue:  
a) Se o campo [matricula](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/#2500_ideTrab_infoContr_matricula) não estiver preenchido, deve ser igual ao código de categoria informado no evento S-2300;  
b) Se [indContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/#2500_ideTrab_infoContr_indContr) = [N] e [infoContr/tpContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/#2500_ideTrab_infoContr_tpContr) for diferente de [6], deve ser um código de categoria compatível com o evento S-2200 (conforme regra de validação abaixo);  
c) Se [indContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/#2500_ideTrab_infoContr_indContr) = [N] e [infoContr/tpContr](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1.2/index.html/#2500_ideTrab_infoContr_tpContr) = [6], deve ser um código de categoria compatível com o evento S-2300 (conforme regra de validação  
  
Dessa forma no sistema será validado os campos **Possui informação no evento S-2190, S-2200 ou S-2300 no declarante** (**indContr**) que deve estar como **Não**, **ou** se o campo **indContr** está como **Sim**, porém o campo **Matricula está em branco**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27498634127255)  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[Artigos RH Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971467-RH-Processos-Trabalhistas)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".*
