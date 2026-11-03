---
content_hash: 1677795f83b91aa1c01b4d8ecc400bf60d4c9b77ef2b99c888b3e16a17b270af
fetched_at: '2026-06-29T00:10:44.478988+00:00'
page_id: '552594813'
product: rm
source: tdn-rm
title: Melhoria na Performance
type: documentation
url: https://tdn.totvs.com/display/LRM/Melhoria+na+Performance
version: 35
---

# **Foram simulados dois cenários de comparativos de reajustes.**

#### **Configurações dos cenários:**

* 18 execuções de jobs simultâneos, [configurado no Alias do RM.exe](https://tdn.totvs.com/pages/viewpage.action?pageId=271400764#SQL-214524341);
* 8 reajustes paralelos, [configurado no parametrizador do TCGI](https://tdn.totvs.com/pages/viewpage.action?pageId=435105185).

###### No Reajuste Revitalizado, somente na primeira execução que o sistema calcula os valores desde a data base da regra para que o sistema possa alimentar a nova tabela de histórico.  Nos demais reajustes, o sistema utilizará esta tabela para melhorar o desempenho e  calcular o próximo reajuste.

###### No Reajuste Mercado/Nova Engine, sempre calcula os valores desde a data base da regra do componente do contrato, independente do número do reajuste que esteja executando, desta forma reduzindo o desempenho do reajuste.

|  |  |  |  |
| --- | --- | --- | --- |
| **218 Vendas** | **Reajuste Mercado** | **Reajuste Revitalizado** | **% Melhoria** |
| **1º Reajuste** | **00:38:07** | **00:20:22** | **46,57%** |
| **Demais Reajustes** | **00:39:40** | **00:12:59** | **66,59%** |

##### **1. Reajuste Mercado (Sql-Server) (Melhoria de Performance 66,59% )**

---

##### **2. Reajuste (Nova Engine) (Oracle)****(Melhoria de Performance 37,76% )**

|  |  |  |  |
| --- | --- | --- | --- |
| **71 Vendas** | **Reajuste (Nova Engine)** | **Reajuste Revitalizado** | **% Melhoria** |
| **1º Reajuste** | **00:21:36** | **00:18:14** | **15,59%** |
| **Demais Reajustes** | **00:22:55** | **00:14:22** | **37,76%** |

---

##### **3. Reajuste (Via Fórmula) (Sql-Server)****(Melhoria de Performance 67,76% )**

|  |  |  |  |
| --- | --- | --- | --- |
| **442 Regras de Vendas** | **Reajuste (Nova Engine)** | **Reajuste Revitalizado** | **% Melhoria** |
| **1º Reajuste** | **03:30:12** | **00:20:52** | **90,48%** |
| **Demais Reajustes** | **03:30:12** | **00:11:45** | **94,29%** |

INTEGRAÇÃO
