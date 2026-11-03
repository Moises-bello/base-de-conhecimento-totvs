---
article_id: 35648955443863
category: Gestão de Transportes (TMS)
content_hash: 2b07f46984600fe1a0a1b40c3e9fc0b2b361441456449e03c05c320a14bc6346
fetched_at: '2026-06-28T22:45:29.513245+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Política Nacional de Pisos Mínimos de Frete
  do Transporte Rodoviário de Cargas
type: support-article
updated_at: '2026-03-23T14:11:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35648955443863-Log%C3%ADstica-Linha-Protheus-TMS-Pol%C3%ADtica-Nacional-de-Pisos-M%C3%ADnimos-de-Frete-do-Transporte-Rodovi%C3%A1rio-de-Cargas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35648947923607) Tempo aproximado para leitura: **00:05:30 min**  
  
**Dúvida**  
O que é a Política Nacional de Pisos Mínimos de Frete e como funciona no **Protheus TMS**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Segundo a **ANTT**, "a Política Nacional de Pisos Mínimos do Transporte Rodoviário de Cargas foi instituída pela **Lei nº 13.703, de 2018**, com a finalidade de promover condições mínimas para a realização de fretes no território nacional, proporcionando uma adequada retribuição ao serviço prestado. Em outras palavras, essa Política pública visa garantir que os fretes praticados sejam suficientes para cobrir, minimamente, os principais custos arcados pelos transportadores na atividade de transporte rodoviário de cargas."  
  
Para melhor compreensão sobre como funciona a Política Nacional de Pisos Mínimos de Frete, recomenda-se a leitura do artigo "**Política Nacional de Pisos Mínimos de Frete do Transporte Rodoviário de Cargas"** disponível na seção **Saiba mais.** Nesse artigo a **ANTT** detalha o que é, como calcular, etapas de implantação, legislação, perguntas frequentes e outras informações que auxiliam na compreensão dessa Política.  
  
Com base nessas regras, é importante destacar que a **ANTT** já realizava a fiscalização do Piso Mínimo de Frete. No entanto, com a nova **Nota Técnica 2025.001 do MDFe**, a **ANTT** passa a contar com novas ferramentas mais robustas para a análise automatizada de fretes contratados abaixo do piso mínimo.  
  
No **TMS Protheus**, os valores dos fretes enviados no **MDFe** são obtidos a partir dos cadastros da **Tabela de Frete a Pagar - TMSA790**, ou da **Tabela de Carreteiro por Rota - TMSA220**. O **TMS Protheus**também dispõe de mecanismos para cadastramento da tabela de frete mínimo com base nos **Tipos de Operações da Viagem,** permitindo parametrizar as tabelas de frete a pagar com base nos valores da **Tabela da ANTT RESOLUÇÃO Nº 6.046, DE 11 DE JULHO DE 2024 - COEFICIENTES DE PISOS MÍNIMOS DE TRANSPORTE RODOVIÁRIO DE CARGA.** O tipo de operação da viagem é considerado junto com a quantidade de eixos do veículo para calcular o Piso Mínimo de Frete.  
  
O **TMS Protheus**também realiza integrações nativas com operadoras de frota que possuem as seguintes regras referente ao Piso Mínimo de Frete:

**TMS Protheus x Pamcard**  
Quando há integração com a **Pamcard**, esta operadora realiza a validação dos valores de frete a pagar conforme a Politica Nacional de Pisos Mínimos de Frete. Esse processo está detalhado na documentação **Frete Mínimo Pamcard (SIGATMS) - Exemplo de utilização** disponível na seção **Saiba mais.**

**TMS Protheus  x Repom Frete** e **TMS x Pagbem**  
Atualmente, não há informações oficiais sobre os mecanismos dessas operadoras que permitam consultas ou validações automáticas relacionadas ao Piso Mínimo de Frete pelo **TMS Protheus**. Caso haja interesse, recomenda-se entrar em contato diretamente com as operadoras para obter mais detalhes.  
  
O **TMS Protheus**por si só, não valida automaticamente se os valores de frete a pagar estão conforme a tabela do Piso Mínimo de Frete. No momento, essa validação ocorre somente quando há integração com a **Pamcard.** Portanto, é fundamental que os valores informados ou calculados nas tabelas de frete a pagar estejam corretamente parametrizados conforme a Tabela da **ANTT** de Piso Mínimo de Frete.  
  
**Importante**  
Foi liberado em fevereiro de 2026 o novo parâmetro **MV\_TMSFRMI** que indica se o Sistema irá permitir frete carreteiro abaixo do frete mínimo. Para que as alterações e criações viagens **TMS x PAMCARD** sejam interrompidas por não atender a consulta do Frete Mínimo, é necessário que o parâmetro seja com conteúdo F.  
  
**Saiba mais**  
Artigo da **ANTT** sobre a Política Nacional de Pisos Mínimos de Frete: [Política Nacional de Pisos Mínimos de Frete](https://www.gov.br/antt/pt-br/assuntos/cargas/politica-nacional-de-pisos-minimos-de-frete)  
Artigo **ANTT** sobre fiscalização do Piso Mínimo de Frete: [ANTT avança na fiscalização do Piso Mínimo de Frete com apoio de novas validações no MDF-e](https://www.gov.br/antt/pt-br/assuntos/ultimas-noticias/antt-avanca-na-fiscalizacao-do-piso-minimo-de-frete-com-apoio-de-novas-validacoes-no-mdf-e)  
Tabela da **ANTT** de Coeficientes de Pisos Mínimos de Frete: [RESOLUÇÃO Nº 6.046, DE 11 DE JULHO DE 2024](https://www.in.gov.br/en/web/dou/-/resolucao-n-6.046-de-11-de-julho-de-2024-571717582)  
Calculadora da **ANTT** de Piso Mínimo de Frete: [Calcular Piso Mínimo de Frete](https://calculadorafrete.antt.gov.br/)  
Documentação do **TMS Protheus**sobre Tipos de Operação da Viagem: [Tipos de Operações da Viagem](https://tdn.totvs.com/pages/releaseview.action?pageId=546676595)  
Documentação do **TMS Protheus**sobre Tabela de Frete a Pagar: [Tabela de Frete a Pagar (TMSA790 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=542152688)  
Documentação do **TMS Protheus**sobre Tabela de Carreteiro: [Tabela de Frete Para Carreteiros (TMSA520 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=542153206)  
Documentação do **TMS Protheus**sobre Tabela de Carreteiro por Rota: [Tabela de Frete Para Carreteiros Por Rota (TMSA220 - SIGATMS)](https://tdn.totvs.com/pages/releaseview.action?pageId=542153217)  
Documentação do Frete Mínimo com Pamcard: [Frete Mínimo Pamcard (SIGATMS) - Exemplo de utilização](https://tdn.totvs.com/pages/releaseview.action?pageId=573202032)   
Parâmetro MV\_TMSFRMI: [MV\_TMSFRMI - Indica se o sistema irá permitir frete carreteiro abaixo do frete mínimo.](https://tdn.totvs.com/pages/releaseview.action?pageId=1043715800)  
  
**Glossário**  
**ANTT** - Agência Nacional de Transportes Terrestres  
**MDFe** - Manifesto de Documentos Fiscais eletrônico  
**TMS** - Transport Management System
