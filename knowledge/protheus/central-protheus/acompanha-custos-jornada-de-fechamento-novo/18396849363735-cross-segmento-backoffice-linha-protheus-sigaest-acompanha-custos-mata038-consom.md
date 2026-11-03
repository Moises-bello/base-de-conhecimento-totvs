---
article_id: 18396849363735
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 5075b1407df81b20963302491766ba5b4e254528ed364365fb6c63b83c76d4cd
fetched_at: '2026-06-28T22:38:48.058306+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Acompanha Custos (MATA038)
  consome qual tipo de licença?
type: support-article
updated_at: '2025-12-15T17:43:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18396849363735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Acompanha-Custos-MATA038-consome-qual-tipo-de-licen%C3%A7a
---

A rotina Acompanha Custos (MATA038) utiliza as licenças do módulo Estoque (SIGAEST) do Protheus e não requer licença adicional. Para usar a nova interface, é essencial configurar a Porta Multiprotocolo no AppServer. Em caso de erro de licença, verifique o parâmetro MV\_HVERAO e, para licença TOTVS Intera, inclua a chave Stateless=1 no AppServer.ini.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18396845399063) Tempo aproximado para leitura: **00:02:00**  
  
**Dúvida**  
Qual tipo de licença é utilizada / consumida pela rotina Acompanha Custos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33.

**Solução**

A rotina **Acompanha Custos (MATA038)** está intrinsecamente ligada ao módulo **Estoque (SIGAEST)** e não exige a contratação de uma licença específica adicional, pois utiliza e consome as mesmas licenças do módulo principal.

Para o pleno funcionamento e utilização da **nova interface** das rotinas do Protheus (adotada na MATA038), é crucial que a Porta Multiprotocolo esteja devidamente configurada no AppServer do ambiente.

### **Configuração da Porta Multiprotocolo**

Para habilitar a nova interface e garantir a comunicação adequada da rotina, realize as seguintes ações:

* **Configuração:** É necessário configurar a **Porta Multiprotocolo** no arquivo `AppServer.ini` do seu ambiente.
* **Referências:** Para informações detalhadas sobre o procedimento de configuração, consulte a documentação oficial da TOTVS:

  [Application Server - Porta Multiprotocolo](https://tdn.totvs.com/x/jIUoI)

  [Porta Multiprotocolo - FAQs](https://tdn.totvs.com/x/AsghIQ)

  [Porta Multiprotocolo - Erros comuns](https://tdn.totvs.com/x/JsghIQ)

### **Tratamento de Erros de Licença**

Caso o acesso à rotina resulte na mensagem de erro: **"Não existe licença disponível no License Server para atender a requisição nesse momento"**, verifique e aplique as seguintes configurações:

#### Parâmetro MV\_HVERAO (Horário de Verão)

* **Verificação:** Certifique-se de que o parâmetro **MV\_HVERAO** esteja criado e configurado corretamente.
* **Função:** Este parâmetro é fundamental para definir se o local físico do servidor está, ou não, em Horário de Verão, influenciando a validação da licença pelo *License Server*.

![HVERAO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19624240949143)

#### **Chave** `Stateless` **(Para Licença TOTVS Intera)**

* **Aplicação:** Se a sua empresa utiliza o modelo de **Licença TOTVS Intera** (consumo de licença por demanda no REST do Protheus), a inclusão de uma chave específica é obrigatória.
* **Ação:** Inclua a chave `Stateless=1` na seção correspondente do arquivo `AppServer.ini`.
* **Documentação:** Para mais detalhes sobre o consumo de licença nesse cenário, consulte a documentação oficial. [Consumo de Licença por demanda no REST do Protheus](https://tdn.totvs.com/x/NGR2Hw)

**Saiba mais**:

[*Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)
