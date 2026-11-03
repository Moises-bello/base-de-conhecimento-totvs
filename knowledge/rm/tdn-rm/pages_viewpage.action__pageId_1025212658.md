---
content_hash: d0bcb49a2672f0cfb81c1e57c8361a7992d6cf66a2358c2a1b12b136382de84c
fetched_at: '2026-06-29T00:05:48.492390+00:00'
page_id: '1025212658'
product: rm
source: tdn-rm
title: TOTVS Assinatura Eletrônica - Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1025212658
version: 5
---

Para habilitar a comunicação e o envio de documentos, é necessário definir qual usuário do TOTVS Assinatura Eletrônica (TAE) será o responsável pelas ações de integração (envio de envelopes e consulta de status).

A configuração é realizada por contexto (**Filial** e **Nível de Ensino**), o que permite flexibilidade para utilizar contas diferentes conforme a estrutura da sua instituição.

**Passo a Passo:**

1. Acesse **Ambiente > Parâmetros > Educacional > Integração > TOTVS Assinatura Eletrônica**.
2. Avance até a etapa de definição de usuário.
3. Informe as credenciais (Login e Senha) de um usuário válido no TAE.

⚠️ **Requisito de Permissão** O usuário informado deve, obrigatoriamente, possuir permissão para **"Gerenciar Documentos"** no portal do TAE.

* Verifique as permissões necessárias na [Documentação Oficial do TAE](https://tdn.totvs.com/display/TAE/Manual+Operacional#fluxo_principal--346242983).

Informação Complementar (Parâmetros Globais)

Caso não seja definido um usuário específico no contexto do Educacional (passo acima), o sistema buscará automaticamente a configuração realizada nos **Parâmetros Globais** (por Coligada).

* Essa configuração serve como um *fallback* (reserva) para garantir que a integração não pare.
* Para saber como configurar o usuário global, consulte a página: [Integração RM x TAE (Parâmetros Globais)](https://tdn.totvs.com/pages/viewpage.action?pageId=562963400).

 Veja Também

---

[Guia de Configuração da integração](https://tdn.totvs.com/pages/viewpage.action?pageId=1036767989)

[Guia de Envio e Gestão de Documentos](https://tdn.totvs.com/pages/viewpage.action?pageId=578823895)

[Guia Assinatura na Rematrícula](https://tdn.totvs.com/pages/viewpage.action?pageId=708104832)

[Guia Assinatura na Matricula - PS](https://tdn.totvs.com/display/LRM/02.06+Assinatura+do+contrato)
