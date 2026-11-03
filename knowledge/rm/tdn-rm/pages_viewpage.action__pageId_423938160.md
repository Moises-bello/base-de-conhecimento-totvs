---
content_hash: a95ab4367b78f58cbf80c86cf56818aad74a133b3c72732529dd86a13dfe9872
fetched_at: '2026-06-29T00:09:25.472279+00:00'
page_id: '423938160'
product: rm
source: tdn-rm
title: Faturamento de Item de Contrato por Medição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938160
version: 5
---

Foi retirada a visibilidade dos campos Número de Movimento de Compra/Venda, para tipo de movimento a ser gerado com a numeração com EDITA. Assim, para cada faturamento da medição a tela do movimento será aberta para que o usuário informe o número do movimento.

1. Acessar o módulo **BackOffice** >> **Gestão de Estoque, Compras e Faturamento** >> **Contratos** >> **Manutenção de Contrato;**
2. Marque um contrato que seja de medição e abra o anexo **Visualizar Medições do Contrato;**
3. Na tela de medições de contratos, selecione a medição que deseja ser faturada e vá em **Processos** >> **Faturamento** **Medição;**
4. A tela que se abrirá não terá o campo **Número Movimento Inicial;**
5. Escolha um **Tipo de Movimento** que esteja parametrizado para **Numeração Movimento = Edita;**
6. Execute o processo e a tela de Movimento se abrirá para que o usuário informe o **Nº do Movimento.**

Importante

**A partir dos patchs** **12.1.2502.212, 12.1.2506.161 e 12.1.2510.100** em contratos com controle orçamentário, não é permitido faturar, em uma única operação, medições com a mesma data de vencimento. Nesses casos, é necessário executar o processo individualmente para cada medição que se enquadre neste cenário.
