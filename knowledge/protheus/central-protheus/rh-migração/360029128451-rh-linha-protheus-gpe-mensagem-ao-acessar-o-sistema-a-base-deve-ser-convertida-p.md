---
article_id: 360029128451
category: RH - Migração
content_hash: 1f7e656f8770180f141226fab3fcf54d5cd8de165706407679361f9062cc7206
fetched_at: '2026-06-28T22:43:46.715347+00:00'
product: protheus
section_id: 360001597531
source: central-protheus
title: 'RH - Linha Protheus - GPE - Mensagem ao acessar o sistema: A base deve ser
  convertida para atender a P12. Verificar a documentação referente ao GPECONV'
type: support-article
updated_at: '2025-07-29T19:59:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029128451-RH-Linha-Protheus-GPE-Mensagem-ao-acessar-o-sistema-A-base-deve-ser-convertida-para-atender-a-P12-Verificar-a-documenta%C3%A7%C3%A3o-referente-ao-GPECONV
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15916835219607)**Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao acessar o sistema após efetuar algum processo abaixo:  
- Atualizações;  
- update de release;  
- Criação de novas Empresas ou Grupo de Empresas.  
É apresentada a mensagem e não é possível prosseguir com o acesso ao sistema **"A base deve ser convertida para atender a P12. Verificar a documentação referente ao GPECONV"**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030148971)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
A mensagem ocorre devido ao parâmetro **MV\_RHCONV** possuir o conteúdo padrão para solicitar a execução da Conversão dos Dados  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
**1.** Certifique-se de que o migrador de versão **GPECONV** foi efetuado anteriormente com sucesso ou já iniciou o uso do **Protheus** na versão **12;**  
  
Em casos de criação de novas Empresas ou Grupo de Empresas e nunca ter utilizado o módulo de **Gestão de Pessoal** (GPE);  
**1.** Acesse o módulo do **Configurador** (**SIGACFG**);  
**2.** Base de Dados>Dicionário>Bases de Dados;  
**3.** Em **Parâmetros**;  
**4.** Busque por **MV\_RHCONV**;  
**5.** Altere o conteúdo do parâmetro de .T. para **.F.**;  
**6.** Após essa manutenção, será possível acessar o sistema normalmente.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360068174814)  
  
**Saber Mais:**  
[Pacote de Expedição Contínua Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download?e=1080347)
