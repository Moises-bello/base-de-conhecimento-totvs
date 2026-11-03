---
article_id: 360018375432
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 8e51f83855329a03c64a78e109e3e396e9b4025755bbb15e9ce2d2862514346d
fetched_at: '2026-06-28T22:38:40.980343+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Tamanho da Mensagem na Nota
  Fiscal C5_MENNOTA e F2_MENNOTA
type: support-article
updated_at: '2026-03-12T19:11:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018375432-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Tamanho-da-Mensagem-na-Nota-Fiscal-C5-MENNOTA-e-F2-MENNOTA
---

**Dúvida**  
Tamanho da Mensagem na Nota Fiscal **C5\_MENNOTA**e **F2\_MENNOTA.**  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**  
As mensagens Complementares à serem levadas para a Nota Fiscal **(F2\_MENNOTA)** podem ser registradas de duas formas:

1 - No Pedido de Vendas através do campo **(C5\_MENNOTA)**:

Deve ser digitado manualmente neste campo do cabeçalho do Pedido a informação desejada.  
A informação deve ser levada ao campo **F2\_MENNOTA** (**o qual precisa estar configurado com o mesmo tamanho).**

Se o campo **F2\_MENNOTA**que grava a informação gerada no **C5\_MENNOTA** do pedido de venda para impressão na nota fiscal estiver com tamanho padrão 60, a mensagem será cortada na nota. Se o texto tem mais de 60 caracteres,  altere via configurador o campo **F2\_MENNOTA**para o tamanho máximo 254 para evitar esse tipo de inconsistência com tamanho de texto.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056482554)

2 - Amarrando a mensagem ao *TES* no campo **F4\_FORMULA**: **F4\_FORMULA** = Mensagem a ser impressa na cluna "Observações" dos Livros Fiscais Registro de Entrada e Saídas. Cadastrar uma fórmula (neste caso é justamente o Texto a ser levado) na rotina **CFGX019** - Fórmulas   
**Obs**.: deve ser registrado o texto entre aspas). E amarrar o código dessa fórmula ao TES **F4\_FORMULA**.

Ao registrar o TES no Pedido de Vendas, é levada a informação para a Nota.

**Caso necessite de mais que 254 caracteres:**

O manual do contribuinte menciona que a **TAG** <Infcpl> Informações complementares da nota pode receber até 5000 caracteres. Porém; existe a limitação da ferramenta de **tamanho máximo de 254 caracteres** no campo.

Caso necessite de mais que 254 caracteres, será necessário criar campos personalizados na Tabela SC5 (similares ao **C5\_MENNOTA**).

Neste caso realize a criação de um (ou mais) campo **MEMO** na tabela SC5; e para que a informação seja impressa no **DANFE**, deve ser personalizado em seu **RDMAKE** da NF-e para chamar os novos campos somando às informações do **F2\_MENNOTA**.  
  
**Importante** : Após a criação do campo memo para discriminação de serviços, verifique também a documentação abaixo da equipe Sped para que o mesmo possa ser impresso   
  
[**Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Discriminação de Serviço com mais de 250 caracteres**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012315132-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Discrimina%C3%A7%C3%A3o-de-Servi%C3%A7o-com-mais-de-250-caracteres?source=search)

**Obs:** Havendo dificuldade na criação do campo via CFG, contatar o Suporte Protheus FRAMEWORK pelo Portal do Cliente.

**Saiba Mais:**

* [**Informação Complementar para a Nota e Alteração de Tamanho do Campo C5\_MENNOTA**](http://tdn.totvs.com/pages/viewpage.action?pageId=238028227)
* [**Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Inclusão-de-nota-fiscal-no-módulo-Faturamento**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010811321-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigafat-Inclus%C3%A3o-de-nota-fiscal-no-m%C3%B3dulo-Faturamento)
