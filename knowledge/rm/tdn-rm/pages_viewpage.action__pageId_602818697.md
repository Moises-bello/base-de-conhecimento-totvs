---
content_hash: 9b91a994cfd737c3641f0bf3664ff6f5af3e59d2fbc965f736d871fa640b3eb6
fetched_at: '2026-06-29T00:10:58.039452+00:00'
page_id: '602818697'
product: rm
source: tdn-rm
title: 14.02 - Processo seletivo - Prova Fácil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=602818697
version: 14
---

Importante

Esta funcionalidade está disponível a partir da versão **12.1.32**.

Informações

O ambiente do Prova Fácil deve estar configurado para utilizar as seguintes configurações:

* Acadêmicos: configurado em três níveis.
  + Nível 1: Área ofertada
  + Nível 2: Etapa
  + Nível 3: Data da prova
* Autenticação SSO: esta autenticação deve estar ativa para a correta geração dos links de acesso a avaliação.

**01. Ativação do Prova Fácil**

Para ativar a integração com o Prova Fácil no cadastro do Processo seletivo, deve-se acessar os parâmetros do Processo seletivo (Processo Seletivo | Cadastros | Processo Seletivo / Venda Online de Cursos | Processo seletivo | Parâmetros | Aba Parâmetros | Aba Integração | Aba Prova Fácil) e marcar o campo "**Utilizar integração com o Prova Fácil**".

**Distribuir prova para os candidatos assim que as inscrições forem confirmadas**: este parâmetro define que caso o Processo seletivo não utilize valor de inscrição o candidato irá receber a prova logo após a sua inscrição, caso possua valor de inscrição, o candidato irá receber a prova assim que o sistema identificar a baixa do pagamento através do processo de "Confirmar inscrições".

false

**Observação**:   
  
Para **ativar/desativar** (marcar/desmarcar o parâmetro **Utilizar integração com o Prova Fácil**) a integração com o Prova Fácil, não pode existir uma "**Área de interesse ofertada**" cadastrada no processo seletivo.

## **02. Acesso a avaliação**

É possível acessar a avaliação gerada para o candidato de duas formas, através de envio de e-mail ou acesso direto pela central do candidato. Em ambos os casos o candidato terá acesso direto a prova, sem requerer autenticação, esta funcionalidade é permitida pelo Prova Fácil através de autenticação SSO, assim que o link for gerado, ele tem validade de 30 minutos, no caso do envio do e-mail deve ser observado este tempo, para acesso via central do candidato não é necessário pois ao acionar o botão de execução da avaliação é feita uma nova validação da autenticação. 

# **Envio de e-mail**

É possível configurar um e-mail contendo o link para a avaliação assim que a inscrição for confirmada ou assim que for executado o processo de alocação de candidatos em locais de prova de acordo com as etapas do processo seletivo.

Caso exista a mensagem configurada no processo seletivo o envio será feito automaticamente.

IMPORTANTE

**O link para a avaliação enviado no conteúdo do e-mail tem validade padrão de 30 minutos (tempo padrão definido pelo Prova Fácil)**, neste caso é recomendado e deve ser orientado aos candidatos que seja utilizado o redirecionamento na Central do Candidato.

Utilize o objetivo de mensagem: Enviar e-mail para o candidato com a prova gerada pelo Prova Fácil utilizando SSO

# **Central do candidato**

Ao acessar a central de candidato, na visão de etapas será exibido o botão "Executar avaliação da etapa" na etapa atual que o candidato estiver, após a execução da avaliação e executado o processo de importação das notas, o botão não será mais exibido, somente será exibido casa exista mais de uma etapa e o candidato seja classificado e alocado para a próxima etapa da área ofertada.
