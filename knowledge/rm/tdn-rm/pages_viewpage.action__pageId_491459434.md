---
content_hash: 2924eabd1456ee8a1ad27bbc1563f466bf600ce844a3c3e173b7e8e63f7020e7
fetched_at: '2026-06-29T00:10:21.684087+00:00'
page_id: '491459434'
product: rm
source: tdn-rm
title: Como gerar retificação do S-1200 para competência atual?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=491459434
version: 1
---

false

**A partir das Versões:**

* 12.1.21
* 12.1.22
* 12.1.23
* 12.1.24

A **retificação** para o eSocial trata-se do reenvio de eventos para correção de determinada informação encaminhada incorretamente.

Para a retificação do evento 'S-1200 - Remuneração de trabalhador vinculado ao Regime Geral de Previd. Social' em que a Competência a ser retificação ainda está em aberto deve-se:

RetificacaoPasso 1

Segundo o MOS 2.5, "[...]a retificação de um evento S-1200 somente será aceita se houver correspondência com o valor líquido informado no S-1210. Caso haja desconformidade de valor, impõe-se excluir o S-1210 antes da retificação do S-1200". Assim, deve-se enviar o evento S-3000 para exclusão do evento S-1210 correspondente ao S-1200 que será retificado.

Para geração do S-3000 acesse **eSocial | Eventos da Folha**, selecione o(s) S-1210 relacionado(s) e selecione **Processos | Gerar Evento de Exclusão (S-3000)**. Em caso de envio da reabertura, o S-3000 só deve ser integração e transmitido após o S-1298 ser aceito pelo RET.

Passo 2

Após ajustar as informações na Folha de Pagamento do funcionário, selecione os eventos S-1200 que serão retificados e selecione **Processos | Gerar Retificação Arquivo eSocial**.

Passo 3

Acesse **eSocial | Gerar XML (Eventos Periódicos)** e execute o processo selecionando o tipo de evento **S-1210 Pagamentos de Rendimentos do Trabalho.**

Passo 4

O sistema não realiza a geração via processo de um novo S-1299. Sendo assim, para fechar novamente o período de apuração, insira o S-1299 manualmente na fila de eventos e gere o XML para envio ao governo.

---

**Saiba Mais**

[Como gerar a retificação da folha de pagamento de meses anteriores?](http://tdn.totvs.com/pages/viewpage.action?pageId=438289252)
