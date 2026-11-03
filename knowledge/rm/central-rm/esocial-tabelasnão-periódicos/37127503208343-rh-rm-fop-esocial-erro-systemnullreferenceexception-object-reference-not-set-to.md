---
article_id: 37127503208343
category: eSocial - Tabelas/Não Periódicos
content_hash: 48aea8b143d55589ed61439fedccd1c18d9e4f83c9a477119b0267ebf6808de7
fetched_at: '2026-06-28T22:47:10.461743+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro System.NullReferenceException: Object reference
  not set to an instance of an object.'
type: support-article
updated_at: '2026-04-08T20:41:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37127503208343-RH-RM-FOP-eSocial-Erro-System-NullReferenceException-Object-reference-not-set-to-an-instance-of-an-object
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37127534861335) **Tempo aproximado para leitura: 00:03:00 min**  
  
  
**Ocorrência**  
Ao gerar o S-2299 e apresentado o seguinte erro System.NullReferenceException: Object reference not set to an instance of an object. at RM.Fop.Dominio.Relatorio.RelatorioEFDBaseRemuneracao.<>c\_\_DisplayClass.<GerarInformacoesFolhaPagtoRescisaoTomador>b\_\_0(RateioTomador x) at System.Linq.Enumerable.WhereSelectEnumerableIterator`2.MoveNext() at System.Linq.Enumerable.FirstOrDefault[TSource](IEnumerable`1 source) at RM.Fop.Dominio.Relatorio.RelatorioEFDBaseRemuneracao.GerarInformacoesFolhaPagtoRescisaoTomador(RegistroRelatorioBase registroPaiDemonstrativo, Funcionario funcionario) at RM.Fop.Dominio.Relatorio.EventoS2299.CalcularCampos() at RM.Fop.Dominio.Relatorio.RelatorioEFDBase.Calcula() at RM.Fop.Esocial.FopEsocialMod.CalcularEvento(RelatorioEFDBase relatorio, FopEventoESocial evento, FopTipoArquivoESocialEnum tipoArquivo, Boolean mapeamentoCampos, String executionId  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**  
Esse incidente ocorre quando o sistema tenta localizar informações de **rateio por tomador de serviços** e não encontra a distribuição de encargos, lotação tributária ou dados de vínculo do funcionário.

As causas mais comuns são:

* Distribuição de **SEFIP/Tomador** inexistente ou inconsistente no período da rescisão;
* Lotação Tributária não gerada ou não aceita no eSocial (S-1020 pendente);
* Histórico de rateio por tomador com registros inválidos.
* Parâmetro **“Utiliza Tomadores de Serviço”** marcado indevidamente no Parametrizador da Folha, sem que a empresa utilize tomadores.

**Solução**  
Para corrigir a ocorrência, realize todas as validações abaixo:

**1. Verificar a Distribuição do SEFIP | Tomador**

O erro pode ocorre porque o sistema não encontra o rateio das verbas para o tomador no período da rescisão.

* Acesse: **Encargos | FGTS | Distribuir Tomador**
* Verifique se a distribuição foi realizada para o **mês/ano da rescisão** do funcionário;

**2. Saneamento da Lotação Tributária (eSocial)**

Funcionário vinculado a tomador/obra exigem **Lotação Tributária válida**.

* Acesse: **eSocial | Lotação Tributária**
* Verifique se a **lotação tributária está cadastrada corretamente**, com todas as informações obrigatórias preenchidas;
* Verifique se a lotação está **vinculada ao tomador/obra e ao funcionário** no período da rescisão;
* Acesse a fila de eventos e verifique se o evento **S-1020**, referente à lotação tributária, foi **gerado e enviado com sucesso ao eSocial**.

**3. Validar o parâmetro “Utiliza Tomadores de Serviço”**

Se a empresa **não utiliza tomadores de serviço**, mas o parâmetro estiver ativo, o sistema tentará buscar rateios inexistentes, gerando o erro.

* Acesse: **Configurações | Parametrizador | Folha Normal | Tomador de Serviços**
* Verifique a opção **“Utiliza Tomadores de Serviço”**:

  + **Marcada** → somente se a empresa realmente utiliza tomadores;
  + **Desmarcada** → se não houver rateio por tomador.

**Importante:**

Esse erro está diretamente ligado ao cálculo da **Base de Remuneração por Tomador**, utilizada nos eventos rescisórios do eSocial.  
Qualquer inconsistência entre **rateio, lotação tributária, histórico do funcionário e parametrização da folha** pode resultar no *NullReferenceException* durante a geração do S-2299.
