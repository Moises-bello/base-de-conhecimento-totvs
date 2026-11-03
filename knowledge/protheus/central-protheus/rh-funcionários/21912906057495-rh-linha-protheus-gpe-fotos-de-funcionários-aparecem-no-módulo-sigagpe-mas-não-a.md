---
article_id: 21912906057495
category: RH - Funcionários
content_hash: be6b51bad90e51fb4ab7b9954482b77e36243156c09c3ce91959882c2e1b6ec4
fetched_at: '2026-06-28T22:43:27.274987+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE -  Fotos de Funcionários aparecem no Módulo SIGAGPE,
  mas não aparecem no Módulo SIGAPON
type: support-article
updated_at: '2025-09-02T13:24:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21912906057495-RH-Linha-Protheus-GPE-Fotos-de-Funcion%C3%A1rios-aparecem-no-M%C3%B3dulo-SIGAGPE-mas-n%C3%A3o-aparecem-no-M%C3%B3dulo-SIGAPON
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21912926805015) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Fotos de Funcionários aparecem no Módulo SIGAGPE, mas não aparecem no Módulo SIGAPON.  
  
**Ambiente**  
TOTVS RH - TOTVS TH (Linha Protheus) GPE Gestão de Pessoal - Todas as versões  
  
**Solução**Esse incidente ocorre por conta da configuração do parâmetro **MV\_REPOSIT**.   
Este parâmetro pode ser configurarado de três formas:

**- MV\_REPOSIT = 1** - Tratamento de forma genérica, ou seja, independente de qual Módulo o usuário acessou o Cadastro de Funcionário ou etc, e realizou a inclusão da imagem, ela será apresentada em qualquer módulo que tiver a mesma rotina para acesso;  
**- MV-REPOSIT = 2** - Tratamento de forma individual, ou seja, se o usuário cadastrou uma imagem no Cadastro de Funcionário pelo módulo Gestão de Pessoal, a imagem só será exibida neste módulo;  
**- MV-REPOSIT = 3** - Tratamento de forma especifica para o Módulo SIGAGPE.

Para visualizar a foto do **Cadastro de Funcionário** em **qualquer módulo**, realize os passos abaixo:  
  
**1 -** Acesse o Configurador - **SIGACFG** no menu **Ambiente > Cadastros > Parâmetros:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21912906013463)  
  
**2 -**Pesquise o parâmetro **MV\_REPOSIT:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21912906015127) **3 -**Configure o parâmetro **MV\_REPOSIT** com a **opção 1,** dessa forma será possível visualizar a imagem em **todos os módulos** que tiverem a mesma rotina:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21991646820119)

Após a configuração do parâmetro com **conteúdo 1**, a foto do **Cadastro do Funcionário** poderá ser visualizada tanto no **SIGAGPE** como no **SIGAPON**:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/21912906026135)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21912906028695)

**Observação:** As imagens salvas no **Repositório de Imagens** devem ter as seguintes configurações:  
- Possuir formato *BitMap*;  
- Conter no máximo 256 cores;  
- Conter formato 85 x 66.

**Saber Mais:**[Framework - Linha Protheus - Repositório de Imagens](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026517334-MP-FRAME-Reposit%C3%B3rio-de-Imagens?source=search)  
[RH - Linha Protheus - GPE - Como Incluir Foto no Cadastro do Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007135072-RH-Linha-Protheus-GPE-Como-Incluir-Foto-no-Cadastro-do-Funcion%C3%A1rio?source=search)  
[RH - Linha Protheus - GPE - Ao imprimir a Ficha de Registro, é exibida a mensagem ARQUIVO/system/arquivo.bmp já existe. Regrava](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002723302-RH-Linha-Protheus-GPE-Ao-imprimir-a-Ficha-de-Registro-%C3%A9-exibida-a-mensagem-ARQUIVO-system-arquivo-bmp-j%C3%A1-existe-Regrava?source=search)  
[RH - Linha Protheus - GPE - Como anexar/ salvar documentos no cadastro do Funcionário dentro do Sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010109291-RH-Linha-Protheus-GPE-Como-anexar-salvar-documentos-no-cadastro-do-Funcion%C3%A1rio-dentro-do-Sistema?source=search)
