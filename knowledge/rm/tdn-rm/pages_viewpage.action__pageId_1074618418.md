---
content_hash: 80394241cd15caea1ede6b4a859be14651e1f9ae07dbb62a106863af5ce40914
fetched_at: '2026-06-29T00:05:54.110243+00:00'
page_id: '1074618418'
product: rm
source: tdn-rm
title: Boleto Híbrido - TOTVS Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1074618418
version: 7
---

# Boleto Híbrido no TOTVS Educacional

A agilidade do PIX com a tradicional segurança do Boleto Registrado. Uma experiência sem atrito para o aluno e automação total para a sua Instituição de Ensino.

## O que é o Boleto Híbrido?

É uma solução moderna de pagamento que unifica o boleto bancário tradicional e o pagamento instantâneo via Pix em um único documento e processo integrado.
O grande diferencial para a sua equipe financeira está nos bastidores: **integração direta com o banco via API**. Isso significa o fim definitivo do envio manual de arquivos de remessa e do processamento de arquivos de retorno.

⚡
Processo simplificado, rápido, rastreável e 100% automatizado!

#### Vantagens Estratégicas

|  |  |
| --- | --- |
| ✓ Flexibilidade | Boleto ou PIX na mesma tela |
| ✓ Confirmação Imediata | Baixa em tempo real |
| ✓ Eficiência Operacional | Sem arquivos de remessa |
| ✓ Rastreabilidade | Sincronismo direto via RM |

### 🔄 Jornada de Cobrança Híbrida: Da Emissão ao Recebimento

01

**Parametrização**

Definição das contas, convênios e serviços da matriz de preços habilitados para o modelo híbrido.

02

**Solicitação**

O responsável financeiro visualiza o débito e solicita a guia pelo Portal do Aluno ou Meu eduCONNECT.

03

**Registro via API**

Chamada síncrona do ERP para o banco, que registra o título e retorna o código de barras, linha digitável e o QRCode Pix.

04

**Disponibilização**

O boleto com layout híbrido é renderizado em tela de forma instantânea.

**💡 Experiência do Aluno Intacta:** Para o usuário final no Portal do Aluno ou Meu eduCONNECT, a usabilidade permanece simples e transparente. A única diferença visível será o layout da fatura atualizada trazendo o **QRCode do PIX próximo do código de barras e da linha digitável**.

**💼 Liberação Comercial:** A fase de testes e implementação ocorre **após a contratação da solução complementar recebe+ Boleto Híbrido**. Certifique-se de que a liberação comercial foi concluída para parametrizar o ambiente.

### ℹ️ Releases homologadas

Para habilitar o Boleto Híbrido no módulo Educacional, o seu ambiente RM deve estar atualizado **a partir da release 12.1.2506 com o patch 321** ou versões superiores listadas abaixo:

12.1.2510.248

12.1.2602.164

12.1.2606.1

### 🛠️ Ações para a Implantação

01.
**Planejar atualização de Ambiente:** Certifique-se de atualizar as bases do RM para os pacotes mínimos exigidos.

02.
**Parametrizar o RM:** Configure os parâmetros a seguir
[TOTVS Gestão Financeira](https://tdn.totvs.com/pages/viewpage.action?pageId=1025225590) ,
[Layout Bancos e Agências](https://tdn.totvs.com/pages/viewpage.action?pageId=1025225609) ,
[Convênios](https://tdn.totvs.com/pages/viewpage.action?pageId=1040976062) ,
[TOTVS Educacional](https://tdn.totvs.com/pages/viewpage.action?pageId=1056932101) e os
[Jobs Fracionáveis](https://tdn.totvs.com/pages/viewpage.action?pageId=1040976302).

03.
**Mapeamento de Serviços:** Identificar e associar no módulo Educacional quais serviços da matriz de preços utilizarão a cobrança híbrida.

**📚 Documentações de Apoio:**

[• Configurações do Boleto Hibrido no Educacional](https://tdn.totvs.com/pages/viewpage.action?pageId=1056932101)
[• TOTVS Gestão Financeira - Contas a Pagar e Receber](https://tdn.totvs.com.br/pages/releaseview.action?pageId=908344227)
[• Recebe+ Boleto Híbrido TechFin](https://tdn.totvs.com/pages/viewpage.action?pageId=864326633)
[• Guia de Parametrização, Homologação e Testes](https://tdn.totvs.com/pages/viewpage.action?pageId=1025225507)
