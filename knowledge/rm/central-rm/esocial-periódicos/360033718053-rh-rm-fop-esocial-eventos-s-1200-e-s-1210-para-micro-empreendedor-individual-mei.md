---
article_id: 360033718053
category: esocial - Periódicos
content_hash: ac7407b55b3bc0f8ac84c86dce483477371763962aebe3f3ef7b96f9842b55e3
fetched_at: '2026-06-28T22:47:09.377877+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Eventos S-1200 e S-1210 para micro empreendedor individual
  (MEI) do RM Fluxus
type: support-article
updated_at: '2024-06-05T11:48:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033718053-RH-RM-FOP-eSocial-Eventos-S-1200-e-S-1210-para-micro-empreendedor-individual-MEI-do-RM-Fluxus
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23965562825623) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**  
Como gerar os eventos **S-1200** e **S-1210** na contratação de **MEI** - categoria **741**, registrado no TOTVS Gestão Financeira?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões

**Solução**  
Conforme o **Manual de Orientação do eSocial**, na contratação de **MEI** - Microempreendedor Individual, quando este prestar serviços de hidráulica, eletricidade, pintura, alvenaria, carpintaria e de manutenção ou reparo de veículos, a pessoas jurídicas, o contratante deverá enquadrá-lo na categoria **741** da **Tabela 1** **– Categoria de Trabalhadores**. Neste caso, o **MEI** deve ser tratado como contribuinte individual, **sem sofrer, no entanto, a retenção da contribuição previdenciária devida por esta espécie de segurado**, e **ser identificado pelo CPF e NIS**. Nos demais casos de contratação de **MEI** por pessoa jurídica, o contratante nada informará no eSocial.

No TOTVS Gestão Financeira, o **MEI** poderá ser registrado como pessoa física ou jurídica, devendo ser seguidos passos distintos para cada um conforme abaixo:  
 **• MEI - Pessoa Física**  
1. Em **Administração de Pessoal | Cliente e Fornecedor**, validar o preenchimento do cli/for confirmando principalmente os campos: **Categoria** e **Data de Nascimento** da aba **Identificação**; **C****ategoria****do Autônomo**, **CBO Autônomo**, **Código da Receita** e **NIT** da aba **Tributos**; **Código da categoria eSocial** da aba **eSocial**;  
2. Ainda no cadastro do cliente/fornecedor, acesse **Anexos | Lançamentos**;  
2.1. Inclua ou edite um lançamento existente (ainda não baixado) e na aba **Valores | Tributos**, calcule o IRRF e o INSS do autônomo;  
2.2. Clique em **Exibir Dados para cálculo do INSS,**delete o valor do campo **Base (Valor)** do grupo **INSS do Empregado** e clique no ícone do raio para zerar o valor calculado;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360042519814)

2.3. Após salvar, os valores de **INSS do Empegador** não serão apresentados;  
3. Acesse **eSocial | Gerar XML** (Eventos Periódicos) e gere os eventos para o período de apuração desejado selecionando o parâmetro **Gerar Autônomos Fluxus/Externos**.  
  
• **MEI - Perssoa Jurídica**  
1. Acesse **Administração de Pessoal | Campos Complementares | Cliente e Fornecedor** e inclua um registro com os seguintes dados;  
1.1. **Nome da coluna**- CPFCOMPLEMENTAR;  
1.2. **Descrição**- CPFCOMPLEMENTAR;  
1.3. **Tamanho**- 11;  
1.4. **Tipo**- Alfanumérico;  
1.5. **Tipo de Texto**- Texto;  
2. Acesse **Administração de Pessoal | Cliente e Fornecedor** e repita todas as validações do passo 1 do **MEI** Pessoa Física, incluindo na validação o campo **CPFCOMPLEMENTAR** da aba **Campos Complementares**;  
3. Repita os passos de 2 a 3 do **MEI** Pessoa Física.  
  
**Importante**  
A partir da versão 12.1.25, será disponibilizado o anexo do eSocial, que irá substituir a aba **Integrações | eSocial**.  
Reforçamos a necessidade de preenchimento dos campos presentes em **Configurações | Parametrizador | eSocial | Autônomos e Externos 1/2** e **Autônomos e Externos 2/2**para correta geração dos eventos.  
  
**Saiba mais**  
Veja mais detalhes e exemplos em [Eventos S-1200 e S-1210 na contratação de MEI - Microempreendedor Individual - Autônomos cadastrados no Financeiro ( a partir da versão 12.1.21)](http://tdn.totvs.com/pages/releaseview.action?pageId=440854853).
