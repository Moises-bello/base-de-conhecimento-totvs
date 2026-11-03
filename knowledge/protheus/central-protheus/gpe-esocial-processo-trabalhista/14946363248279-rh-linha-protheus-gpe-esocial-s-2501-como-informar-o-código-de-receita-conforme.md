---
article_id: 14946363248279
category: GPE - eSocial - Processo Trabalhista
content_hash: c64be4424affab67fca4202d15d74e44dd01c90c6b73ffaca12c6f172bd01878
fetched_at: '2026-06-28T22:45:00.613727+00:00'
product: protheus
section_id: 10604669539479
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2501 - Como informar o código de receita,
  conforme tabela 29 do leiaute S-1.1
type: support-article
updated_at: '2024-06-19T18:06:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14946363248279-RH-Linha-Protheus-GPE-eSocial-S-2501-Como-informar-o-c%C3%B3digo-de-receita-conforme-tabela-29-do-leiaute-S-1-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como informar o código de receita, conforme tabela 29 do leiaute S-1.1, para geração da tag [infoCRContrib](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/index.html#r_2501_ideTrab_calcTrib_infoCRContrib) no evento S-2501?  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Na tag **InfoCRContrib**, conterá informações das contribuições sociais devidas à Previdência Social e Outras Entidades e Fundos, por **Código de Receita - CR**. Conforme estipulado no MOS S-1.1.  
Deve ser gerado no xml do evento S-2501 a tag **tpCR** que significa o **Código de Receita - CR** relativo a contribuições sociais devidas à Previdência Social. Tem como validação: Deve ser um código válido e existente na [**Tabela 29**](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/tabelas.html#29).  
E após a tag tpCR, devemos informar a **tag vrCR**, com o **valor correspondente ao Código de Receita - CR.**  
Validação: Deve ser informado de acordo com a legislação em vigor na competência. Deve ser maior que 0 (zero).  
  
Para preencher as informações que serão levadas nas tags citadas, acesse a rotina **Dados eSocial (TAFA552D)** e selecione **Tributos (S-2501).**O sistema demostrará os processos cadastrados, clique para **Editar** conforme imagem abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14945176508439)  
  
Clique novamente para **Editar**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14945245494551)  
  
Nessa tela pode-se editar ou incluir período:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14945305712279)  
  
Selecione a opção **Incluir Contribuição Social**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14945319691159)  
  
Selecione o **Código de Receita** e informe o **Valor**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14945395430935)  
  
 **Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[RH - Linha Protheus - GPE - eSocial - Processos Trabalhistas - Premissas para geração dos eventos de processos trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13317899021847)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
