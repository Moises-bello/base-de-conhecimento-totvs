---
article_id: 360043726414
category: Controle de Documentos (SIGAQDO)
content_hash: 65325d54daf7d5630ffdd502e8c95888932ed3462404e9acf0bf09e63e0b3f20
fetched_at: '2026-06-28T22:42:28.998309+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Desconexão por inatividade quando alterado
  o documento no Word
type: support-article
updated_at: '2021-05-12T13:26:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043726414-Manufatura-Linha-Protheus-SIGAQDO-Desconex%C3%A3o-por-inatividade-quando-alterado-o-documento-no-Word
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Quando configurado a variável **InactiveTimeOut** no arquivo **appserver.ini** e o usuário está editando o documento no **Word**, por que o Sistema desconecta por inatividade?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Por padrão, a edição do documento no **Word** irá respeitar o tempo definido na variável **InactiveTimeOut**, porém, existe o parâmetro **MV\_QDOTOWO - Habilita TimeOut nas integrações do SIGAQDO com o Word** que permite configurar o Sistema, para que desconsidere o tempo de *timeout* quando o usuário estiver editando o documento no **Word**.  
  
O parâmetro **MV\_QDOTOWO**, por padrão terá conteúdo igual à **.T.**, mas para que o Sistema não desconecte por inatividade, o parâmetro deve ser alterado para **.F.**.  
  
**Saiba mais**  
A configuração deste parâmetro está disponível em [Configuração Parâmetro MV\_QDOTOWO](https://tdn.totvs.com/x/U07sF)
