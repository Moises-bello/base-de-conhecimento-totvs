---
article_id: 360016579352
category: RH - Funcionários
content_hash: a4fe2761c7994f092cc103c4ce1480e0b7b0510f99fc0f6428bb375ec0fa0b81
fetched_at: '2026-06-28T22:43:27.377179+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Ao tentar selecionar supervisor no cadastro de
  Informações exclusivas de Estágio o Sistema não localiza nenhum participante/funcionário
type: support-article
updated_at: '2025-08-18T19:39:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016579352-RH-Linha-Protheus-GPE-Ao-tentar-selecionar-supervisor-no-cadastro-de-Informa%C3%A7%C3%B5es-exclusivas-de-Est%C3%A1gio-o-Sistema-n%C3%A3o-localiza-nenhum-participante-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34272256095639)** Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**No módulo **Gestão de Pessoal**, ao tentar **selecionar supervisor** no **cadastro de Informações exclusivas de Estágio** o sistema **não localiza nenhum participante/funcionário**.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Esse incidente ocorre, pois não foi feito relacionamento de funcionários no Cadastro de Participantes (**APDA020**) no módulo **Avaliação e Pesquisa de Desempenho (SIGAAPD)**

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Através da Rotina **APDA020** (Cadastro de Participantes)**,**clique no menu**Outras Ações**e em**Relacionar Participantes,** conforme abaixo:  
  
**![](https://totvssuporte.zendesk.com/attachments/token/Xf4X4lXD1zVwgS8sSJSWxr6MA/?name=inline-454219687.png)​​**  
2. Selecione a opção **Relacionar**, e clique em **Salvar**;  
  
![](https://totvssuporte.zendesk.com/attachments/token/tgdjWEk5Z4aFH3sIYGSdwy1lE/?name=inline2004393436.png)​  
  
3. Informe se deseja relacionar funcionários desligados ou não;  
  
  
![](https://totvssuporte.zendesk.com/attachments/token/cfwreB0T03xDRzvlPTZOKYljU/?name=inline1986908127.png)​  
  
**Observações:**

A relação será atualizada com as informações dos funcionários que constam na tabela **SRA, é obrigatório que o funcionário tenha CPF informado no cadastro.**  
  
Acesse através da rede do windows a pasta***system*,** localizada na pasta de bases do Protheus, e verifique se consta arquivo **MSRELRDZ**(Parâmetros de configuração .INI). Caso não conste, baixe o arquivo em anexo e coloque dentro da pasta ***system*** e refaça o relacionamento.  
  
**Saber Mais:**

[RH - Linha Protheus - GPE - Como realizar cadastro de Estagiário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016561192-RH-Linha-Protheus-GPE-Como-realizar-cadastro-de-Estagi%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Como renovar contrato de estagiário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052079934-RH-Linha-Protheus-GPE-Como-renovar-contrato-de-estagi%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Mensagem ao cadastrar estagiário: A Entidade escolhida não possui todos os campos necessários preenchidos, para contemplar o cadastro Informações do Estagiário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403056683287-RH-Linha-Protheus-GPE-Mensagem-ao-cadastrar-estagi%C3%A1rio-A-Entidade-escolhida-n%C3%A3o-possui-todos-os-campos-necess%C3%A1rios-preenchidos-para-contemplar-o-cadastro-Informa%C3%A7%C3%B5es-do-Estagi%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Calculo para estagiário mensalista](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056843894-RH-Linha-Protheus-GPE-Calculo-para-estagi%C3%A1rio-mensalista?source=search)

[RH - Linha Protheus - GPE - Como calcular rescisão de um estagiário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015970332-RH-Linha-Protheus-GPE-Como-calcular-rescis%C3%A3o-de-um-estagi%C3%A1rio?source=search)

[RH - Linha Protheus - GPE - Como alterar a Escola/Entidade de um Estagiário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4424966290711-RH-Linha-Protheus-GPE-Como-alterar-a-Escola-Entidade-de-um-Estagi%C3%A1rio?source=search)
