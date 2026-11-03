---
article_id: 37781639489175
category: eSocial - Eventos Totalizadores
content_hash: 8d7ae2bf8e972e8beb371fb9c17cc52b1c22ed22320470bf4558cecbb543ff40
fetched_at: '2026-06-28T22:47:06.968072+00:00'
product: rm
section_id: 1500000834481
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware: Relatório de Conferência de Dados Complementares
  IRRF  S-5002'
type: support-article
updated_at: '2026-05-26T14:10:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37781639489175-RH-RM-FOP-eSocial-Middleware-Relat%C3%B3rio-de-Confer%C3%AAncia-de-Dados-Complementares-IRRF-S-5002
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37781622875927) Tempo aproximado para leitura: **00:02:00min**  
  
**Dúvida**  
Como configurar e gerar o novo Relatório de Conferência de Dados Complementares de IRRF para identificação de divergências entre Folha de Pagamento e eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir dos pacotes 12.1.2502.267, 12.1.2506.228, 12.1.2510.157 e superiores.   
  
**Solução**  
O Relatório de Conferência de Dados Complementares de IRRF tem como objetivo principal auxiliar na identificação de eventuais divergências entre os valores de IRRF presentes no envelope de pagamento e os valores reportados pelo RET.

Os dados apresentados são o resultado de uma análise comparativa entre os valores de IRRF enviados do RH ao governo por meio dos eventos S-1200, S-1202, S-1207, S-2299 e S-2399, e os valores que o Governo retorna por meio do evento S-5002.

**Itens disponíveis para conferência:**  
**•** Bases de cálculo segmentadas por Código de Receita;  
**•**Valores de Pensão Alimentícia;  
**•**Previdência Complementar;  
**•**Assistência Médica e Odontológica (Plano de Saúde);  
**•**Reembolsos de despesas com saúde.

📚 **Documentação**  
  
Abaixo segue **documentação com orientações** de como configurar e gerar o relatório para **clientes Middleware**:

* [Middleware - Relatório de Conferência IRRF S-5002](https://tdn.totvs.com/pages/viewpage.action?pageId=1028947938)

Para clientes **TAF Full** (TAF padrão), verificar o documento abaixo:

* [TAF - RELATÓRIO - Relatório de Conferência da DIRF (IRRF), S-5002](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37326283758487)

🖥️ **Evento Webinar**

Veja abaixo a gravação do evento TOTVS Responde realizado sobre o tema:

* [Espaço Legislação | DIRF Mensal | TOTVS RH Linha RM](https://www.youtube.com/watch?v=bBMHvp8NQGQ)

**Importante**  
**1.** Para que o relatório seja gerado corretamente, é necessário que os eventos de remuneração tenham sido encaminhado pelo Middleware e conste o evento de retorno S-5002 no RM(evento S-1210 com status 10 - aceito RET;  
**2.** Após atualização do pacote, faz-se necessário rodar o **RM.Atualizador;**  
**3.** Na parametrização (etapa 2 [**Middleware - Relatório de Conferência IRRF S-5002**](https://tdn.totvs.com/pages/releaseview.action?pageId=1028947938#1-1) **)** o servidor **api/app** deve ser o caminho do servidor que foi atualizado a patch para atender a geração do relatório.

**Saiba mais**  
Para mais informações, acesse:

* [DIRF Mensal - Espaço Legislação](https://espacolegislacao.totvs.com/dirf-mensal)
* [How To | Relatório de Conferência de IRRF](https://www.youtube.com/watch?v=4j2ZIAIS56I)
* [Configurando DefaultDB](https://tdn.totvs.com/display/public/LRM/Configurando+DefaultDB)
* [Configuração do API e APP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044519633)
* [RM Atualizador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5893403025687?source=search)
