---
article_id: 29396880696599
category: Configurações
content_hash: c4ef7ac39503cf5a8c7d9061828837a99a8da49cf157de8dfaea22f80e19da72
fetched_at: '2026-06-28T22:46:49.449222+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Fracionamento de Jobs - Atualiza Campo Desconto Simplificado
type: support-article
updated_at: '2025-01-21T19:10:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29396880696599-RH-RM-FOP-Fracionamento-de-Jobs-Atualiza-Campo-Desconto-Simplificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29396880675863) Tempo aproximado para leitura: **00:01:14 min** **Dúvida**Como realizar o Fracionamento de Jobs para a rotina Atualiza Campo Desconto Simplificado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento

a partir dos patchs/Release abaixo:

12.1.2402.267

12.1.2406.222

12.1.2410.153

12.1.2502 e superiores

**Solução**Foi implementado o recurso de Fracionamento de JOBs para o processo Atualiza Campo Desconto Simplificado no módulo TOTVS Folha de Pagamento.

Para Habilitar o recurso é necessário:

1. Configure o Host ou Service Host com a tag **JobServer3Camandas= True**
2. Em **Parametrizador | Folha Normal | Geral**, marcar o parâmetro **Habilita Fracionamento de Jobs**
3. Acesse **Ambiente | Processos | Segurança de Jobs Fracionáveis**,  e inclua a classe **FopAtualizaCampoDescontoSimplificadoProcess**  
     
   Preenchimento dos campos da tela:  
     
   **- Campo Perfil:**  informe o perfil que terá acesso ao processo.  
     
   **- Classe do Job:** FopAtualizaCampoDescontoSimplificadoProcess  
   **- Min. Frações:**  insira o valor 2  
     
   **- Máx. Frações:** insira um valor maior que 2. Recomenda-se aumentar o valor gradativamente para otimizar a performance do processo.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29396880679575)

Para obter acesso à configuração completa do Fracionamento de Jobs , por favor, **[CLIQUE AQUI](https://tdn.totvs.com.br/display/public/LRM/TOTVS+Folha+de+Pagamento+-+Fracionamento+de+Jobs)**.  
  
**Saiba mais**[RH - RM - FOP - Habilitar Fracionamento de Jobs](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9912971569559-RH-RM-FOP-Habilitar-Fracionamento-de-Jobs)  
[RH - RM - FOP - Atualiza Campo Desconto Simplificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29372557131671-RH-RM-FOP-Atualiza-Campo-Desconto-Simplificado)
