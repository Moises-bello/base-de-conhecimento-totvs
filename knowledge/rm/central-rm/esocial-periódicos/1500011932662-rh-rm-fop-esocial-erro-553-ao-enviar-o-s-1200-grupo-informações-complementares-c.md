---
article_id: 1500011932662
category: esocial - Periódicos
content_hash: 93cef88176ef04e0b66451dac19d143429d294ff9bb640cecafeacec574054c8
fetched_at: '2026-06-28T22:47:09.283606+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 553 ao enviar o S-1200: Grupo Informações complementares
  contratuais do trabalhador não deve ser preenchido'
type: support-article
updated_at: '2026-01-26T15:58:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011932662-RH-RM-FOP-eSocial-Erro-553-ao-enviar-o-S-1200-Grupo-Informa%C3%A7%C3%B5es-complementares-contratuais-do-trabalhador-n%C3%A3o-deve-ser-preenchido
---

**![](https://totvssuporte.zendesk.com/attachments/token/cm2qACg3aYlUf5pRKkFBWAa4v/?name=inline-1079383826.png)**

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Conforme Layout do eSocial, a *tag* **infoComplCont** deve ser preenchida se a categoria for igual a [2XX, 304,  
305, 4XX, 7XX, 902]) e se para o trabalhador não houver evento S-2300 ativo) E (se não for informado remunPerApur/matricula ou remunPerAnt/matricula)); OC ((se codCateg = [901, 903, 904]) E (se para o trabalhador  
não houver evento S-2300 ativo) E (se não for informado remunPerApur/matricula ou remunPerAnt/matricula));  
não obrigatório nos demais casos.

Sendo assim, se o funcionário for de categoria cujo envio do S-2300 não for obrigatório, o sistema verifica se existe ou não o S-2300 na fila de eventos. Encontrando o S-2300, a tag **infoComplCont** não é gerada no XML.

Outra validação a ser realizada é se o S-2300 está na Fila de Eventos Complementar. Em caso positivo, siga os passos abaixo para restaurá-lo à fila padrão e gerar novamente o evento periódico:  
1. Acesse **Folha de Pagamento | Fila de Eventos Complementar** aplique um filtro para a chapa do funcionário;  
2. Localize o S-2300 correspondente e copie o identificador do evento;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484553793687)

3. Acesse **Folha de Pagamento | Fila de Eventos Complementar | Restauração da Fila de Eventos do eSocial,** insira o **Identificador** que foi copiado no passo 2 e execute a rotina;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484553798423)

4. Gere novamente o XML **S-1200** integre e transmita ao governo.  
  
**Importante**  
Para as versões superiores à **12.1.25.250,** **12.1.26.200** ou **12.1.27.143** a geração do evento S-1200 foi ajustada para que considere os registros existentes na **Fila de Eventos do eSocial Complementar**.   
Documentação válida para leiaute eSocial a partir da versão S-1.0  
  
**Saiba mais**  
Para mais informações sobre **Fila de Eventos Complementar** acesse:  
      • [Restaurar fila de eventos complementar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036243133-RM-eSocial-Restaurar-fila-de-eventos-complementar?source=search)
