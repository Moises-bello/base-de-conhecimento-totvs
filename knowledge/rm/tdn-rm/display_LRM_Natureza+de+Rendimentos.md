---
content_hash: c9b681a0bfdaaaa32fb15c48729873accc98e9d2e09cd25df9c667101f9a5e77
fetched_at: '2026-06-29T00:10:30.901132+00:00'
page_id: '520111918'
product: rm
source: tdn-rm
title: Natureza de Rendimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Natureza+de+Rendimentos
version: 23
---

# Conteúdo

3trueConteúdo

# 1. Introdução

Conforme definido no *Anexo I dos leiautes da EFD-Reinf - Tabelas versão 2.1.1*, as retenções de imposto de renda decorrentes do rendimento de trabalho devem ser enviadas pelo eSocial. No entanto, para situações específicas em que não seja possível fazer o envio pelo eSocial, a EFD-Reinf deve ser a escrituração utilizada para essa apuração. Maiores detalhes a respeito estão informados nos manuais de orientação do eSocial e da EFD-Reinf.

Nestes casos, as retenções devem ser classificadas com um código da Natureza do Rendimento, conforme lista preestabelecida pela Receita Federal do Brasil

# 2. Natureza de Rendimentos

No RM, é necessário realizar o cadastro da Natureza de Rendimento para que ele seja utilizado nas retenções registradas nos Documentos Fiscais ou nos Lançamentos Financeiros. Para isso, basta acessar o cadastro, informar o código e uma descrição para a Natureza de Rendimentos e marcar ou desmarcar a opção "**Sem IR",** conforme necessidade.

Ao incluir um Movimento/Lançamento Financeiro com uma Natureza de Rendimento cujo campo "**Sem IR**" esteja marcado, apenas o valor bruto será gerado na EFD-Reinf. Os valores referentes à retenção não serão gerados, mesmo que estejam preenchidos no tributo.

Para acessar o cadastro da natureza de rendimentos, vá em TOTVS Gestão Fiscal | Cadastros | Específicos - Mais | Natureza de Rendimentos

# 3. Outras informações

* É possível vincular uma natureza de rendimento em uma situação tributária ou em seus itens. Para isso, acesse a aba "Outros Tributos", insira ou edite um tributo existente e preencha o campo "Identificador da Natureza de Rendimento".
* Ao informar o item de movimento, o sistema irá considerar a seguinte ordem de prioridade para preenchimento da Natureza de Rendimento, do item:  
  1 - Natureza de Rendimento informada no Anexo - Dados Fiscais do Produto;  
  2 - Natureza de Rendimento informada no Anexo - Tributos Defaults de Cli/For;  
  3 - Natureza de Rendimento informada no parâmetro do tipo de movimento.  
    
  Obs: Esta regra é considerada para os tributos **PISRF**, **COFINSRF**, **COSIRF**, **CSLLRF**, **CSRF**, **IRRF** e **IRRF Importação**.
