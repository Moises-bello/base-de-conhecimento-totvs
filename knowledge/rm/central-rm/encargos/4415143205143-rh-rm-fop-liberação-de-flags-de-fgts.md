---
article_id: 4415143205143
category: Encargos
content_hash: 457f9ffeeabaa36deedf25d4dbc000782507c2b01dab038f74daa34661caded1
fetched_at: '2026-06-28T22:46:53.202259+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Liberação de Flags de FGTS
type: support-article
updated_at: '2025-03-11T11:15:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415143205143-RH-RM-FOP-Libera%C3%A7%C3%A3o-de-Flags-de-FGTS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:50 min****Dúvida**Como realizo a liberação de flags de FGTS? **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**A liberação de flags é um dispositivo utilizados para detectar, se houve, alguma alteração na ficha cadastral do funcionário. Realizando este procedimento o sistema limpará as flags e atualizará.  
  
Por exemplo: houve mudança no número da carteira de trabalho do funcionário. Após gerar o arquivo para recolhimento do FGTS, será necessário fazer a liberação de flag para limpar a informação da ficha cadastral, para que não sejam enviados os mesmos registros de alteração no próximo recolhimento de FGTS. Para a liberação, acesse a aba Encargos | Liberação de Flags de FGTS:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9551309331095)  
  
Clicando sobre a opção, o sistema irá apresentar uma tela de parametrização. Nela, Defina o "Código de quebra":  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9551421335191)  
  
Em seguida, clique em "Seleção de Funcionários" para acessar a janela de seleção:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9551425469335)  
  
É importante ressaltar por default todos os itens virão selecionados, mas se desejar que somente sejam liberados os flags da alteração do nome do funcionário, por exemplo, deixe marcado somente aquele ao qual o corresponde. Ao finalizar o processo de liberação, o sistema exibirá o número de funcionários que foram processados e um resumo de erros/avisos.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9551480677527)  
  
**Importante**Caso seja necessário enviar informações que tenham a flag marcada, ao entrar no módulo poderá ser selecionado apenas as opções para liberação da flag. Por exemplo, Precisa ser liberada a flag do Número do PIS e não pode liberar a flag do Endereço de Correspondência. Basta desmarcar o parâmetro do Endereço de Correspondência que a flag do mesmo continua marcada internamente e será informada a alteração no arquivo do SEFIP. Este procedimento se faz necessário, por exemplo, para admitidos no mês. Pode ser feito para outros campos também. Por exemplo, se quer informar a mudança de dados somente da Carteira de Trabalho, desmarque o parâmetro da Carteira de Trabalho e deixe todos os outros marcados que somente a flag da Carteira de Trabalho não será liberada. O mesmo serve se for para um funcionário apenas, que neste caso deve fazer o filtro na seleção do funcionário que a flag continuará marcada.
