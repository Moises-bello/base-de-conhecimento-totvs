---
content_hash: c42be48adb50ef5db062cccc0fefaa5407c96267e184c932c65b44e6ae99628f
fetched_at: '2026-06-29T00:11:21.167000+00:00'
page_id: '689058315'
product: rm
source: tdn-rm
title: Configurações e geração do Relatório do Espelho Assinatura Eletrônica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=689058315
version: 20
---

## **01. VISÃO GERAL**

Para gerar o Relatório do Espelho será necessário conceder a permissão dos usuários que irão utilizar a integração de documentos com o TOTVS Assinatura Eletrônica e nos parâmetros globais informar a URL da integração com o Totvs Assinatura Eletrônica.

## **02. EXEMPLO DE UTILIZAÇÃO**

11Configurações

Para o funcionamento da integração, o usuário necessitará realizar algumas configurações iniciais , abaixo relacionadas:

1 – Contratação de um plano de assinaturas através da TOTVS Store, que pode ser acessada através do endereço abaixo:

**[TOTVS Assinatura Eletrônica - Trial](https://partner.totvs.store/br/produto/catalog/product/view/id/911/s/totvs-assinatura-eletronica-trial/)**

2-Criação dos usuários que realizarão as integrações através do TOTVS Automação de Ponto, podendo assim consultar status, excluir documentos e outros que assim se fizer necessário no Totvs Assinatura Eletrônica.

3-Parametrizar o sistema para realizar a comunicação com o TOTVS Assinatura Eletrônica.

No Automação de ponto permitir acesso as opções de Assinatura Eletrônica, através do Cadastro -Perfis.

É obrigatório cadastrar os tipos de URL´s  em Ambiente-Parâmetros -Parâmetros Globais para a integração com o Totvs Assinatura eletrônica. Deverá selecionar o tipo 30 -Integração com Totvs Assinatura Eletrônica.

Campo **URL de autenticação**: Deverá ser informada a URL de autenticação .

Camo **URL da API de Integração**:Deverá ser informada a URL da API .

Campo **URL de login via formulário Web**: Deverá ser informada a URL de login via formulário Web.

## 

2Geração do Relatório do Espelho do cartão

Após concluída as configurações, será visualizado no menu Relatório do Espelho do cartão o Parâmetro "**Enviar relatório para assinatura eletrônica**".

**Importante:**

* Ao Assinalar o **"Enviar relatório para assinatura eletrônica"** o parâmetro "Gerar relatório em PDF" ficará marcado e desabilitado.
* Ao retirar a permissão no perfil do usuário no item 09.02.01-Relatório do espelho do ponto o parâmetro não será mais visualizado, desta forma, será gerado o relatório padrão.
* Para a integração com o TAE da assinatura eletrônica é obrigatório o Relatório do espelho possuir o formato PDF .
* Se o funcionário não tiver e-mail cadastrado, será demonstrada mensagem no log na  geração do Relatório do espelho.

solidExemplos

**Exemplo 1: Geração do Relatório do espelho enviando ao Totvs Assinatura Eletrônica:**

Acessar o menu Relatório do espelho do cartão ou individualmente e realizar a geração confirmando a opção "**Enviar relatório para assinatura eletrônica**".

Ao concluir a geração , será visualizado no monitor de Relatórios o Documento Pendente para assinatura

O funcionário irá acessar o Totvs Assinatura Eletrônica (TAE) e visualizará as mesmas informações ainda pendentes.

No Totvs Automação de Ponto o funcionário terá a ação: Assinar.

Selecionando a opção “Assinar”, será demonstrada a seguinte informação:

Atente-se a informação apresentada na tela cor Amarela.

Será apresentada a opção **Próxima Etapa** ,informe o Tipo da assinatura "**Assinar eletronicamente**"  e estando de acordo confirme o campo "Declaro que li e concordo em realizar a assinatura do documento", em seguida selecione  **Assinar documento** ou **Rejeitar**.

No final do processo , será demonstrada para o usuário a mensagem: Documento assinado com sucesso! E o status é alterado de Pendente para Finalizado.

O funcionário poderá visualizar o documento assinado no Totvs Assinatura Eletrônica ao selecionar a opção "**Visualizar**" -**Baixar assinado**.

Será demonstrado o relatatório do espelho e no final do relatório o Protocolo de Assinatura.

**Exemplo 2: Relatório Espelho: Funcionário não possui e-mail cadastrado**

1-Funcionário não possui e-mail cadastrado

Gerando o Espelho do cartão.

No passo 3 marque o parâmetro “Enviar relatório para assinatura Eletrônica”.

No final da geração será demonstrada log com a mensagem: Não foi possível enviar o relatório para a assinatura eletrônica. Funcionário não possui e-mail cadastrado.

##
