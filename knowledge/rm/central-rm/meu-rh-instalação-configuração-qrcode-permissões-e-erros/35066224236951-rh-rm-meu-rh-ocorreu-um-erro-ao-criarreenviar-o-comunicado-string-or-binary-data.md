---
article_id: 35066224236951
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: ce135f0f01b5b1e7e45fcadde347ad478d3319b495b5d07becca82b4e3186826
fetched_at: '2026-06-28T22:47:29.454623+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Ocorreu um erro ao criar/reenviar o comunicado. - String
  or binary data would be truncated
type: support-article
updated_at: '2025-09-23T15:00:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35066224236951-RH-RM-Meu-RH-Ocorreu-um-erro-ao-criar-reenviar-o-comunicado-String-or-binary-data-would-be-truncated
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35066192061591) Tempo aproximado para leitura: **00:02:35 min**  
  
**Ocorrência**  
Ao tentar enviar um comunicado é apresentado a mensagem de erro " Ocorreu um erro ao criar/reenviar o comunicado. - String or binary data would be truncated ".  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) – Meu RH – A partir da versão 12.1.2502.  
  
**Causa**  
Esse incidente ocorre porque a quantidade de caracteres informada em algum campo do comunicado ultrapassa o tamanho máximo definido na estrutura da tabela no banco de dados. Ou seja, está sendo inserido uma String (texto) maior do que o permitido para aquele campo.  
   
Motivos mais comuns:

* Título ou conteúdo do comunicado com excesso de caracteres.
* Campos internos (como nome da empresa, departamento, função etc.) cujo conteúdo somado ultrapassa o limite.
* Erros em campos configuráveis pela TOTVS, geralmente causados por customizações que não ajustaram corretamente os limites de tamanho.

**Solução**  
Verifique se algum dos campos preenchidos ultrapassa o limite de caracteres. Neste exemplo, como o comunicado será enviado para todos os cargos, não é necessário selecionar todos na opção **Função**, pois já foram definidos a filial e o departamento. Os filtros devem ser utilizados apenas quando houver necessidade de restringir a comunicação a funcionários específicos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35066224222999)

**Saiba mais:**  
[Comunicados para o RH](https://tdn.totvs.com/display/NPR/33.0+Comunicados+para+o+RH)
