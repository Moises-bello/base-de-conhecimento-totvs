---
content_hash: 5a311b12f17847c0f5aae9c78fd5b2327fea670c422102ad3faefd2fa3fa4163
fetched_at: '2026-06-29T00:10:52.200401+00:00'
page_id: '570997503'
product: rm
source: tdn-rm
title: Como gerar a diferença salarial no mês da rescisão no evento S-1200?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570997503
version: 8
---

false

**A partir das Versões:**

* 12.1.27.292
* 12.1.28.205
* 12.1.29.129

# Objetivo:

---

Atender as orientações do eSocial, quando no mês da rescisão houver diferença salarial por dissídio e o evento S-2299 já estiver sido enviado ao governo. Neste caso será necessário enviar um evento S-1200. Veja mais detalhes no MOS do eSocial.

Apresentaremos abaixo os procedimentos necessários para a geração da diferença salarial no evento S-1200.

11Execução do scriptExecução do script

Para a liberação do campo "Pagamento de dissídio na competência do desligamento após o envio do S-2299"  será necessário executar o script através do sistema RM.Atualizador.exe.

true2Lançamento da diferençaLançamento da diferença

Ao gerar a rescisão complementar marque o parâmetro "Pagamento de dissídio na competência do desligamento após o envio do S-2299".

**Atenção:**

Este parâmetro deve ser marcado somente quando o pagamento do dissídio for realizado na mesma competência da demissão do funcionário e após ter enviado o evento S-2299 para o governo. Marcando este parâmetro, as informações do dissídio serão levadas no evento S-1200.

Se fizer o lançamento do dissídio sem marcar este parâmetro, caso o pagamento do dissídio seja na mesma competência da demissão do funcionário, será necessário fazer uma retificação do evento S-2299 para contemplar as informações do dissídio.

Após o calculo da rescisão complementar com o parâmetro marcado basta gerar o xml periódico S-1200 para o funcionário.

falseImportante

* o gatilho dos eventos periódicos não será gerado automaticamente, será necessário executar a rotina "Gerar xml".
