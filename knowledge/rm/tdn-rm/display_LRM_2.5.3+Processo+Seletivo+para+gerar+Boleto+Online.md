---
content_hash: a6baa07b362e33614634bf3ea06b875b6b2cb5fcec3d01ad16f641947cbab5fe
fetched_at: '2026-06-29T00:10:43.715005+00:00'
page_id: '550327166'
product: rm
source: tdn-rm
title: 2.5.3 Processo Seletivo para gerar Boleto Online
type: documentation
url: https://tdn.totvs.com/display/LRM/2.5.3+Processo+Seletivo+para+gerar+Boleto+Online
version: 9
---

Acesse o cadastro através do *Educacional | Processo Seletivo* para parametrizar as informações financeiras. Informar toda a configuração de geração de lançamento para as inscrições, das abas "Geral 1" e "Geral 2". Para mais informações acesse o link abaixo:

* **Boleto Registrado**

**Parametrizar Processo seletivo para gerar Boleto Registrado Online**

**1º-** Configurar o convênio da Conta/Caixa de acordo com o documento abaixo, para registro online:

* <https://tdn.totvs.com/x/LeIdGQ>

**2º-**Acesse o cadastro de processo seletivo para cadastrar as informações financeiras.

Informar toda a configuração de geração de lançamento para as inscrições, das abas "Geral 1" e "Geral 2".

**TOTVS Processo Seletivo | Cadastros | Processo seletivo/Venda Online de Cursos | Aba Informações Financeiras**

**3º-**Por fim, marcar o parâmetro "Gerar lançamentos/boletos com registro online" e informar o campo "Convênio" que foi parametrizado anteriormente.

**Obs.:** O campo "Apresentar boleto de cobrança registrada ainda não registrado no Portal" deve estar DESMARCADO.

Após realizada toda a parametrização, é possível "Testar Geração de Lançamento" para identificar erros ou mesmo inconsistências nas informações.

Regra válida a partir da versão 12.1.33.278 /12.1.34.143.

Para ambientes configurados para registrar o boleto online, o registro irá ocorrer somente quando o boleto for emitido, ou seja, no portal do processo seletivo quando o candidato clicar em “**Pagar via boleto**”, ou na central do candidato quando for clicado em “**Boleto**”.

Essa regra será aplicada somente quando o processo seletivo estiver parametrizado para que o tipo de relatório seja "**PDF – TOTVS Report**” (**Aba Parâmetros| SubAba Geral 2/3**).

**Importante:**

Para que o registro ocorra com sucesso é necessário que o**TOTVS Gestão Financeiro** esteja com o parâmetro “**Convênio Default para o Registro Online Boleto**” preenchido (Mais detalhes: [FIN - Contas a receber](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+receber)).
