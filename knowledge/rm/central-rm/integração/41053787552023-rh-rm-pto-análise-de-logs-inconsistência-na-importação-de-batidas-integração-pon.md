---
article_id: 41053787552023
category: Integração
content_hash: 5989fac7fdc31f8af3b0762982188965bbf97c2f7934e25ada641ecb2ae36020
fetched_at: '2026-06-28T22:46:34.603108+00:00'
product: rm
section_id: 6045439793431
source: central-rm
title: 'RH - RM - PTO - Análise de Logs: Inconsistência na importação de batidas -
  Integração Ponto RM x Clockin'
type: support-article
updated_at: '2026-06-08T15:35:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41053787552023-RH-RM-PTO-An%C3%A1lise-de-Logs-Inconsist%C3%AAncia-na-importa%C3%A7%C3%A3o-de-batidas-Integra%C3%A7%C3%A3o-Ponto-RM-x-Clockin
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41053801996311) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar a análise detalhada dos logs de integração quando as batidas de ponto efetuadas no Clockin não são importadas para o espelho de ponto do funcionário no RM TOTVS Automação de Ponto?

**Ambiente**  
Cross Segmento - TOTVS RH (Linha RM) - Automação de Ponto - Versão 12.1.28 e superiores  
  
**Solução**  
Para identificar a causa da ausência das marcações no espelho de ponto do colaborador, deve-se executar inicialmente uma tentativa de importação manual e completa do período.  
Durante a parametrização desse processo, é indispensável desmarcar a opção que orienta o sistema a considerar o último NSR importado, selecionando de forma manual e exata as datas que compreendem o período mensal do ponto do funcionário.   
  
![clockin1png.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41053787510423)  
Assim que o processamento for concluído, o sistema exibirá o resultado e o relatório técnico diretamente na tela. O operador deve obrigatoriamente salvar todas as informações geradas, o que envolve os arquivos de Avisos, Erro (caso a opção seja exibida), Log Técnico Carol, Padrão e os Parâmetros de Importação, consolidando-os em um arquivo de texto utilizando o bloco de notas para posterior verificação.  
  
![Clockin2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41053802001815)  
Com os arquivos devidamente salvos e tendo em mãos a chapa do funcionário no RM e o respectivo número de CPF, o usuário deve iniciar a validação minuciosa de cada documento para compreender o motivo do impedimento da integração. No log de Parâmetros da Importação, é primordial certificar-se de que não existem informações adicionais incorretas, garantindo que os campos destinados ao terminal do relógio e ao endereço do arquivo permaneçam completamente limpos e vazios.

Segue um exemplo do log Parâmetros da Importação sem informações externas, somente da integração:

\*\*\*\*\*\*\* Parâmetros da Importação de Batidas \*\*\*\*\*\*\*\*

Coligada..............: 1

Layout de Relógio.....: CAR

Terminal do Relógio...:

Endereço do arquivo...:

Considera última linha: Não

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
  
Exemplo do log Parâmetros da Importação **com** informações externas:  
  
\*\*\*\*\*\*\* Parâmetros da Importação de Batidas \*\*\*\*\*\*\*\*  
Coligada..............: 1  
Layout de Relógio.....: 0004  
Terminal do Relógio...: 001  
Endereço do arquivo...: C:\AFD.txt  
Considera última linha: Não  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
  
Note que os campos de Layout do Relógio, Terminal do Relógio, Endereço do arquivo estão preenchidos, e um detalhe que o layout não é o padrão do Clockin (CAR). Isso ocorre devido a ter salvo o perfil de parâmetros com informações de um arquivo AFD junto com a integração, ocasionando nesta situação. Portanto, deverá deixar um perfil de parâmetros somente para a integração e que os campos e filtros estejam "limpos":  
  
![clockin3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41053787519767)

Isso garante que não haja nenhuma interferência "externa" durante o processo de importação via integração.  
  
Na sequência, ao inspecionar o log de Avisos, o operador deve realizar uma busca focada na chapa do funcionário e na data correspondente à marcação, avaliando se há alertas específicos que justifiquem a retenção do registro.

A continuidade do diagnóstico deve ocorrer no log de nome Padrão, utilizando o CPF do colaborador como chave de busca para avaliar o comportamento do sistema no dia do evento, confrontando o NSR da batida e o dispositivo utilizado pelo funcionário, o que também permite analisar o código do terminal para identificar eventuais inconsistências no próprio aparelho.

Por fim, o Log Técnico fornecerá os subsídios mais profundos sobre a comunicação entre as plataformas, permitindo o rastreamento por CPF, código do dispositivo, NSR, data ou nome do colaborador. É nesse ambiente que se analisam os detalhes de erros complexos e se confirma a integridade da comunicação, validando se houve o estabelecimento de conexão bem-sucedido entre os servidores do Clockin e do RM por meio do status 200.

**Saiba mais**

Para aprofundamento nos conceitos de integração entre as plataformas e arquitetura de comunicação de dados, o usuário pode consultar os manuais e guias conceituais de produtos unificados disponíveis nos repositórios oficiais de documentação da TOTVS.  
Acesse: [Base de conhecimento RM TOTVS Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000860722-Automa%C3%A7%C3%A3o-de-Ponto-CHRONUS)  
  
Erros e situações comuns que podem ocorrer na integração que podem ser identificados na análise dos logs:  
[RH - RM - PTO - Erro Incorrect login or password na integração com Clockin](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37059977420951-RH-RM-PTO-Erro-Incorrect-login-or-password-na-integra%C3%A7%C3%A3o-com-Clockin)  
[RH - RM - PTO - Erro ao importar batidas na integração com a Carol/Clock In](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062421874-RH-RM-PTO-Erro-ao-importar-batidas-na-integra%C3%A7%C3%A3o-com-a-Carol-Clock-In)  
[RH - RM - PTO - "Lacuna de NSR" quando se utiliza o parâmetro de Considera o Último NSR Importado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36550653133463-RH-RM-PTO-Lacuna-de-NSR-quando-se-utiliza-o-par%C3%A2metro-de-Considera-o-%C3%9Altimo-NSR-Importado)

**Importante**

Se após a conferência e análise detalhada de todos os arquivos de log não for possível determinar a causa exata para a não importação das marcações, a TOTVS disponibiliza suporte especializado por meio de seu serviço de consultoria técnica. Caso o cliente opte por esse direcionamento corporativo para obter o acompanhamento dedicado de um analista focado em seu cenário de negócios, basta sinalizar a necessidade diretamente no atendimento para que sejam iniciados os trâmites comerciais de elaboração e aprovação do orçamento.
