---
content_hash: 9d319d8531e774302aa1259555619855d8f24f39d282ba99a437840d07b0b04c
fetched_at: '2026-06-29T00:05:52.123476+00:00'
page_id: '1056932101'
product: rm
source: tdn-rm
title: Configurações do Boleto Hibrido - TOTVS Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056932101
version: 8
---

A partir das versões **12.1.2506.268, 12.1.2510.187, 12.1.2602.111 e 12.1.2606.1** será possível a utilização do boleto híbrido no educacional

**Pré-requisitos**

Para habilitar a funcionalidade no sistema e garantir a configuração adequada do **Boleto Híbrido** no módulo **Gestão Financeira**, é fundamental revisar as diretrizes e regras apresentadas na documentação oficial:

* [Boleto Híbrido](https://tdn.totvs.com/pages/viewpage.action?pageId=908344227)
* [Regras Funcionais](https://tdn.totvs.com.br/pages/releaseview.action?pageId=908344227#0-8 "Follow link")
* [Guia de QR Code no RM Reports](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028429732-Cross-Segmentos-Backoffice-RM-BI-QRCode-no-RM-Reports "Follow link")

Além disso, vale temos alguns pontos importantes com relação ao Boleto Híbrido que devem ser levados em consideração:

* **Processo de Registro:** Ao gerar um lançamento no módulo **Educacional**, ele não será classificado automaticamente como híbrido. O registro deve ser realizado manualmente através da visão de boletos, acessando o menu: **Boleto Híbrido > Registrar Boleto Híbrido.**
* **Registro via Portal do Aluno:** Caso as parametrizações estejam corretas, o registro também poderá ocorrer de forma automática quando o aluno acionar a opção de pagamento via boleto no **Portal do Aluno.**
* **Identificação do Status:** Para confirmar se o título foi convertido com sucesso, verifique a coluna **Status da Remessa** na visão de boletos. O campo deverá apresentar a descrição: **"Registrado boleto híbrido".**
* **Restrição de Data:** Por regra do módulo **Gestão Financeira**, não é permitido o registro de boletos híbridos com data de vencimento inferior à data atual.

Parametrizações

Após a configuração no módulo **Gestão Financeira**, será possível configurar, no módulo **Educacional**, o relatório para impressão do boleto híbrido, disponível no caminho:

**Ambiente > Parâmetros > Educacional > Tesouraria > Relatórios**

A falta de configuração do relatório de boleto híbrido impedirá a emissão do documento no Portal, gerando uma mensagem de erro ao aluno. Note que as configurações são independentes: o funcionamento do boleto convencional não supre a ausência do híbrido, e vice-versa. Ambos devem estar parametrizados para garantir a disponibilidade total.

A criação do relatório pode ser realizada conforme as orientações disponíveis na seção **[Dúvidas Frequentes](https://tdn.totvs.com/pages/viewpage.action?pageId=908344227#0--305990429:~:text=Como%20parametrizar%20o%20relat%C3%B3rio%20do%20boleto%20h%C3%ADbrido%20com%20c%C3%B3digo%20de%20barras%20e%20qr%20code%20pix%3F).**

Além disso, o lançamento no qual o boleto híbrido será utilizado deve estar vinculado a uma **Conta/Caixa** cujo **convênio** esteja devidamente configurado.

Para definir qual Conta Caixa será utilizada no lançamento deve verificar no caminho: **Ambiente > Parâmetros > Educacional >Integração > Financeiro (Fin - Geral 2/4).**

Após a realização das configurações descritas acima e o [registro do boleto](https://tdn.totvs.com/pages/viewpage.action?pageId=908344227#0-3:~:text=2.%20Registro%20Online%20do%20Boleto%20H%C3%ADbrido), ele poderá ser gerado e visualizado no **extrato financeiro** e demais rotinas de pagamento do portal do aluno.

Caso o convênio esteja configurado corretamente e o boleto ainda não esteja registrado, o registro será realizado automaticamente ao clicar na opção **Gerar Boleto**.

Além disso, o código de barras poderá ser visualizado ao clicar na opção **Gerar código de barras**, permitindo também a sua cópia para utilização no pagamento.
